# Named Entity Recognition(NER)

A named entity is a “real-world object” that’s assigned a name – for example, a person, a country, a product or a book title. 

For example, for a text: `Apple is looking at buying U.K. startup for $1 billion.`
|Text   |Start| End |Label  |Description|
| ----------- | ----------- | ----------- | ----------- |----------- |
Apple   |0  |5  |ORG    |Companies, agencies, institutions.|
U.K.    |27 |31 |   GPE |Geopolitical entity, i.e. countries, cities, states.|
$1 billion  |44 |54 |MONEY| Monetary values, including unit.|

Here, the word Apple is the organization, the word the UK is a geopolitical entity or country, and $1 billion is money. 

# Custom Named Entity Recognition model to identify disease name form clinical data using spaCy V3.2

The project develops a custom Named Entity Recognition model with spaCy. The custom model can recognize the disease name from the clinical text.
# Dataset Description
To develop the custom NER model, we will use clinical text form [Biobert](https://github.com/dmis-lab/biobert) data on Github. 

They have provided a pre-processed version of datasets on NER:
* [Named Entity Recognition:](https://drive.google.com/file/d/1OletxmPYNkz2ltOr9pyT0b0iBtUWxslh/view) (17.3 MB), eight datasets on biomedical named entity recognition.


If you want to download the data manually:
1. Open the following google drive link
   *  https://drive.google.com/file/d/1OletxmPYNkz2ltOr9pyT0b0iBtUWxslh/view
  
2. Download the zip file and then extract the data inside the NERdata folder.

We are programmers; therefore, we will download the dataset by writing python code. Before that, let's install the required package on a virtual environment and then we will download the data through code.

### Install Virtual Environment

1. Install `virtualenv` package.

    ```sh
    pip3 install virtualenv
    ```
    Now let's clone the repository using the terminal.
    ```sh
    git clone git@github.com:kshitizregmi/NER-on-biomedical-disease-data.git
    ```

2. Goto NER-on-biomedical-disease-data folder and open the terminal and type 

    ```sh
    virtualenv disenv
    ``` 
    to initialize the virtual environment on the project folder.


3. After this, you will need to activate the virtual environment to start working on the project through the terminal. Use the following command:

    ```sh
    source disenv/bin/activate
    ``` 

    Once you do this, your prompt will change and it will show (disenv on the beginning of the absolute path of your project folder)

4. Install all required packages listed on requiremnts.txt

    ```sh
    pip3 install -r requirements.txt
    ``` 
    The project setup is complete now, let's download the data using code.


### Download data using code

You can download data through code using the following command:
```sh
python3 download_data.py
```
The above command will download all data in [Named Entity Recognition:](https://drive.google.com/file/d/1OletxmPYNkz2ltOr9pyT0b0iBtUWxslh/view).

Here, we will only use the `BC5CDR-disease dataset.` In the dataset, `train_dev.tsv`, `test. tsv`, `train.tsv` are the data for validation, testing and training, respectively.

### Inside train.tsv

<center>
<img src = "https://drive.google.com/uc?export=view&id=184BsKaYyecW5CPTqO2OkipADebIOpUNw"/>
<figure caption >Figure 1: Clip of training data </figure caption>
</center>

Here,
*  B: Begin entity, 
*  I: Inside entity and,
*  O: Outside entity

spaCy doesn't support this format of data. Therefore we have to convert data to a spaCy readable format. To convert data into spacy format the method `load_data_spacy()` inside `format_to_spacy.py` is used. 


# How to train a custom NER model ?


We will train the custom NER model by using spaCy English pipeline `en_core_web_md` optimized for CPU. 

To train the custom NER model run the following command on terminal/bash.

```python 
python3 train.py
```
At the end of the training, i.e. after 20 epochs, the custom NER model is saved on folder `models` as `disease_model`. Additionally, It stores the f1-score of test data and validation data calculated while training the model on the `score` folder as `test_f1scores.json` and `valid_f1scores.json`, respectively.


# Results


We can load the dumped f1-scores on the `score` folder to visualize validation and test accuracy. You can plot the accuracy using the following command:

```python
python3 plot.py
```
After running the above command, you will see an Image like this:

<center>
<img src = "https://drive.google.com/uc?export=view&id=1-u7K5tNJhcCZDeAaYSnZ7STh8oL3cHJu"/>
<figure caption >Figure 2: F1- score on validation and test data </figure caption>
</center>


# How to Infer the output

To visualize the output on our custom data we will use the following code. The same code is written in the `disp_output.py` file. You can run the `python3 disp_output.py` command to visualize the result.


```python
import spacy
from spacy import displacy

from spacy import displacy
MODEL_PATH = 'models/disease_model'
ner = spacy.load(MODEL_PATH)
text = "Selegiline - induced postural hypotension in Parkinson ' s disease : a longitudinal study on the effects of drug withdrawal.The aims of this study were to confirm our previous findings in a separate cohort of patients and to determine the time course of the cardiovascular consequences of stopping selegiline in the expectation that this might shed light on the mechanisms by which the drug causes orthostatic hypotension"
doc = ner(text)
# displacy.render(doc,jupyter=True, style = "ent")
displacy.serve(doc, style="ent")
```

For the given input text, the output from the custom NER model looks like the following image:

<img src = "https://drive.google.com/uc?export=view&id=1mW1gZjUlwjxQoF8jHsxpHi0mrr5L_Ter"/>
<figure caption >Figure 3: NER to detect disease form input text </figure caption>

You can see the image like above by opening `http://0.0.0.0:5000` on your browser after you run the command `python3 disp_output.py`.

# References
* [Named Entity Recognition using Spacy and Tensorflow](https://aihub.cloud.google.com/u/0/p/products%2F2290fc65-0041-4c87-a898-0289f59aa8ba)
* [Biobert](https://github.com/dmis-lab/biobert)
* [💥 Out now: spaCy v3.2 ](https://spacy.io)
* [Custom Named Entity (Disease) Recognition in clinical text with spaCy 2.0 in Python](https://github.com/rsreetech/CustomNERwithspaCy)
