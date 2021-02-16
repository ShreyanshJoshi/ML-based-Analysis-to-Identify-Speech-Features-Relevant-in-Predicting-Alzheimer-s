# Alzheimer's-Detection-by-Speech-Analysis

Alzheimer’s disease (AD) is a progressive neurodegenerative disease that affects nearly 50 million individuals across the globe and is one of the leading causes of deaths worldwide. The average age of onset is around 65 years and common symptoms include memory loss, language impairment, behavioural changes, decline in physical and
social abilities, and eventually the inability of the patient to function independently. There is no cure for the disease per se, and the current medication and management strategies can only try to slow down the progression and improve symptoms.

But, wouldn't it be better, if we can make prescient predictions as to whether a person has AD (or could have in the future) just by analysing the speech of that person ? Analysing speech does not require any sophisticated equipments, is non-invasive, can be done quickly and is inexpensive, making it highly scalable. Therefore, we in this project, work on detection of Alzheimer’s disease using speech analysis with machine learning and deep learning based models.

### Dataset - 
We acquired transcripts of conversations with people, many of whom had different forms of dementia, in CHAT Format (Codes for the Human Analysis of Transcripts) from DementiaBank’s Pitt Corpus. The transcripts were parsed using the CLAN software to extract features specific to our needs. The following commands were used -
* IPSYN for Syntactic Complexity
* EVAL for Word-type ratios, Grammatical Analysis and Count of Utterances
* FLUCALC for Fluency and Pauses

After the use of these commands, all extracted features were stored in a single CSV file that had about 1200 entries and 100+ features. This data was thoroughly cleaned by dropping off redundant columns and dealing with NaN values as well as some errors we found in data. The data was also standardized before training our models, so as to avoid any unwanted bias to certain features.

### Methodology - 
We decided to train multiple classifiers to compare their accuracies of prediction using speech factors. We trained multi-class classifiers (classifying into 6 stages of AD) as well as binary classifiers (classifying into 'control' and having AD) since some classes had too little samples for the models to learn anything useful. The following models were trained and tested - 

* XGB Classifier
* Support Vector Classifier
* Decision Trees
* Random Forests
* K-Nearest Neighbours
* Neural Networks (ANNs)

For all the classifiers, we plotted a normalized confusion matrix to analyse their performance and compare them.
