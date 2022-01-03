from format_to_spacy import load_data_spacy
TRAIN_DATA, LABELS = load_data_spacy("NERdata/BC5CDR-disease/train.tsv")
print("Length of Training data is {}".format(len(TRAIN_DATA)))
TEST_DATA, _ = load_data_spacy("NERdata/BC5CDR-disease/test.tsv")
print("Length of Training data is {}".format(len(TEST_DATA)))
VALID_DATA, _ = load_data_spacy("NERdata/BC5CDR-disease/train_dev.tsv")
print("Length of Training data is {}".format(len(VALID_DATA)))

# # some example data of train set are

# print("Trainset data exmaple: {}".format(TRAIN_DATA[:5]))