# ML based Analysis to Identify Speech Features Relevant in Predicting Alzheimer’s 

Alzheimer’s disease (AD) is a progressive neurodegenerative disease that affects nearly 50 million individuals across the globe and is one of the leading causes of deaths worldwide. The average age of onset is around 65 years and common symptoms include memory loss, language impairment, behavioural changes, decline in physical and
social abilities, and eventually the inability of the patient to function independently. There is no cure for the disease per se, and the current medication and management strategies can only try to slow down the progression and improve symptoms.

But, wouldn't it be better, if we can make prescient predictions as to whether a person has AD (or could have in the future) just by analysing the speech of that person ? Analysing speech does not require any sophisticated equipments, is non-invasive, can be done quickly and is inexpensive, making it highly scalable. Therefore, we in this project, work on detection of Alzheimer’s disease using speech analysis with machine learning and deep learning based models.

### Dataset - 
We acquired transcripts of conversations with people, many of whom had different forms of dementia, in CHAT Format (Codes for the Human Analysis of Transcripts) from DementiaBank’s Pitt Corpus. The transcripts were parsed using the CLAN software to extract features specific to our needs. The following commands were used -
* IPSYN for Syntactic Complexity
* EVAL for Word-type ratios, Grammatical Analysis and Count of Utterances
* FLUCALC for Fluency and Pauses

After the use of these commands, all extracted features were stored in a single CSV file that had about 1200 entries and 100+ features. This data was thoroughly cleaned by dropping off redundant columns and dealing with NaN values as well as some errors we found in data. The data was also standardized before training our models, so as to avoid any unwanted bias to certain features. Eventually we had 50 features that were used to train the models.

### Methodology - 
We decided to train multiple classifiers to compare their accuracies of prediction using speech factors. We then trained both binary classifiers (Control and Probable AD) as well as multi-class classifiers to distinguish Alzheimer’s disease from normal aging and other neurodegenerative diseases. The following models were trained and tested - 

* XGB Classifier
* Support Vector Classifier
* Decision Trees
* Random Forests
* K-Nearest Neighbours
* Neural Networks (ANNs)

For all the classifiers (both binary & multi-class), we plotted a normalized confusion matrix to analyse their performance and compare them. 4 different performance metrics were used: accuracy, recall, F1-score and precision to get a thorough understanding of which model performs the best really. Also, then we come to the main goal of this project: studying feature importances in predicting Alzheimer's in our models. We plotted feature importance graphs for each model, to find which speech features are important for a particular model in making predictions.

In both multi-class and binary classification, ANN was found to outperform the other models with a testing accuracy of 76.44% and 92.05% respectively. For the feature importance part, it was observed that ‘%_PRESP’ (present participle tense), ‘%_3S’ (3rd person present tense markers) were two of the most important speech factors for our classifiers in predicting Alzheimer’s.
