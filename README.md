Sentiment Analysis of Twitter Data
=============

Sentiment analysis (also known as opinion mining) refers to the use of natural language processing, text analysis and computational linguistics to identify and extract subjective information in source materials. The code given in the repository is implemented in python and is using Naive Bayes Classifier and also it's improved version. 

This was built in Python 3.4 and please refer to the pre-requistes required for running it successfully. 

Pre-requisites - 
-------
1. Python 3.4 (although it shoudn't have problem running on other Python versions apart from some syntax changes)
2. NLTK for Python 
3. Stopwords corpus
4. Wordnet corpus

Usage - 
-------
1. Clone/Download zip of SentAnalysis.
2. Extract content of the zip.
3. Run mainFile.py in IDLE or cmd and you would see the following -  

```
Enter file name: twitterData.csv #Enter the filename(enter path also if stored in another location)

Enter number of records to be read: 5000 #The top n records will be taken from the dataset for creating the model

Processing..

NBC or improved NBC? Enter NBC/iNBC:
(Improved NBC takes into account high information words and removes the low information words, cutoff set to 5) - iNBC

Improved NBC is running..

Accuracy = 75.15974440894568%

Enter sample text to determine sentiment: @VirginAmerica completely awesome experience last month BOS-LAS nonstop. Thanks for such an awesome flight and depart time. #VAbeatsJblue
positive
```
