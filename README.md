# Named Entity Recognition(NER)

A named entity is a “real-world object” that’s assigned a name – for example, a person, a country, a product or a book title. 

For example, for a text: `Apple is looking at buying U.K. startup for $1 billion.`
|Text   |Start| End |Label  |Description|
| ----------- | ----------- | ----------- | ----------- |----------- |
Apple   |0  |5  |ORG    |Companies, agencies, institutions.|
U.K.    |27 |31 |   GPE |Geopolitical entity, i.e. countries, cities, states.|
$1 billion  |44 |54 |MONEY| Monetary values, including unit.|

Here, the word Apple is the organization, the word the UK is a geopolitical entity or country, and $1 billion is money. 

# Custom Named Entity Recognition model to identify disease name form clinical data using spaCy

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
