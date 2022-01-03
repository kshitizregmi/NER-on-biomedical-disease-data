import spacy
from spacy.util import minibatch, compounding

import random

from load_and_visualize_data import *
from metric import evaluate

from spacy.training import Example

def print_metric(f1_score, precision, recall):
    print('F1-score = {}'.format(f1_score))
    print('Precision = {}'.format(precision))
    print('Recall = {}'.format(recall))
    
def train_spacy(train_data, labels, iterations, dropout = 0.5, display_freq = 1):
    ''' Train a spacy NER model, which can be queried against with test data
   
    train_data : training data in the format of (sentence, {entities: [(start, end, label)]})
    labels : a list of unique annotations
    iterations : number of training iterations
    dropout : dropout proportion for training
    display_freq : number of epochs between logging losses to console
    '''
    valid_f1scores=[]
    test_f1scores=[]
    nlp = spacy.load("en_core_web_md")
    #nlp = spacy.blank('en')
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    else:
        ner = nlp.get_pipe("ner")
   
    # Add entity labels to the NER pipeline
    for i in labels:
        ner.add_label(i)

    # Disable other pipelines in SpaCy to only train NER
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):
        #nlp.vocab.vectors.name = 'spacy_model' # without this, spaCy throws an "unnamed" error
        optimizer = nlp.create_optimizer()
        for itr in range(iterations):
            random.shuffle(train_data) # shuffle the training data before each iteration
            losses = {}
            batches = minibatch(train_data, size = compounding(16.0, 64.0, 1.5))
            for batch in batches:
                texts, annotations = list(zip(*batch))
                example = []
                # Update the model with iterating each text
                for i in range(len(texts)):
                    doc = nlp.make_doc(texts[i])
                    example.append(Example.from_dict(doc, annotations[i]))
            
                nlp.update(example,
                    drop = dropout,  
                    sgd = optimizer,
                    losses = losses)
                
            score = evaluate(nlp,VALID_DATA)
            precision = score['precision']
            recall = score['recall']
            f1_score = score['f1score']
            valid_f1scores.append(f1_score)
            print('================================================')
            print('Epochs = {}'.format(itr))
            print('Losses = {}'.format(losses))
            print('===============ON VALIDATION DATA=======================')
            print_metric(f1_score, precision, recall)
            score = evaluate(nlp,TEST_DATA)
            precision = score['precision']
            recall = score['recall']
            f1_score = score['f1score']
            test_f1scores.append(f1_score)
            print('===============ON TEST DATA========================')
            print_metric(f1_score, precision, recall)
            print('================================================')
            
    return nlp,valid_f1scores,test_f1scores



ner,valid_f1scores,test_f1scores = train_spacy(TRAIN_DATA, LABELS,20)

ner.to_disk("models/disease_model")

# dump test and valid f1 scores

import json
# dump test and valid f1 scores

with open('scores/valid_f1scores.json', 'w', encoding = "utf-8") as f:
    f.write(json.dumps(valid_f1scores))

with open('scores/test_f1scores.json', 'w', encoding = "utf-8") as f:
    f.write(json.dumps(test_f1scores))