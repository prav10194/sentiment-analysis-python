# Main File
from correctingReplacingWords import ExtractingData
from classifierNBC import ClassifyData
import classifierNBC1
from tagAndLemmatize import TaggingAndLemmatize
import nltk
from nltk.classify import NaiveBayesClassifier

class ClassificationOfData:

    def run(self):

        location=input('Enter file name: ')
        file=open(location,encoding="utf8").readlines()
        sents,labelsData=self.correctAndReplaceData(file)
        option=input('\nNBC or improved NBC? Enter NBC/iNBC: \n(Improved NBC takes into account high information words and removes the low information words, cutoff set to 5) - ')
        classifierNBC=self.classifierNBCData(sents,labelsData,option)
        print(classifierNBC.labels())
        classifyText=input('Enter sample text to determine sentiment: ')
        classifyText=ExtractingData().runMethods([classifyText])
        classifyText=TaggingAndLemmatize().LemmatizeSents(classifyText)
        for cT in classifyText:
            if option=='iNBC':
                print(classifierNBC.classify(classifierNBC1.wordDict(nltk.tokenize.word_tokenize(cT))))
            else:
                print(classifierNBC.classify(ClassifyData().wordDict(nltk.tokenize.word_tokenize(cT))))
        input('')
        
    def correctAndReplaceData(self,file):
        sents=[]
        k=1
        labelsData=[]
        numb=input('Enter number of records to be read: ')
        print('Processing..')
        for a in file:
            if len(a.split(","))==3 and k<int(numb):
                labelsData.append(a.split(",")[0])
                sents.append(a.split(",")[2])
                k=k+1
        sentsED=ExtractingData().runMethods(sents)
        sentsTAL=TaggingAndLemmatize().LemmatizeSents(sentsED)
        return sentsTAL,labelsData

    def classifierNBCData(self,sents,labelsData,option):
        if option=='iNBC':
            print('Improved NBC is running..')
            return classifierNBC1.implementMethods(sents,labelsData,'a')
        else:
            print('NBC is running..')
            return ClassifyData().implementMethods(sents,labelsData,'a')

ClassificationOfData().run()
