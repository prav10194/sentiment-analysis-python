#Implement NaiveBayesClassifier
import nltk
from nltk.classify import NaiveBayesClassifier
import collections
from nltk.classify.util import accuracy
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist

class ClassifyData:

    def wordDict(self,words):
        return dict([(w,True) for w in words])

    def featureList(self,sents,labelsData):
        featuresDict=collections.defaultdict(list)
        k=0
        #print(type(sents))
        #print(sents[0])
        for sent in sents:
            #print(type(sent))
            w=nltk.tokenize.word_tokenize(sent)
            #print(w)
            featuresDict[labelsData[k]].append(self.wordDict(w))
            k=k+1
        return featuresDict

    def setSplit(self,lf,split=0.75):
        train=[]
        test=[]
        for label,feats in lf.items():
                cutoff=int(len(feats)*split)
                train.extend([(feat,label) for feat in feats[:cutoff]])
                test.extend([(feat,label) for feat in feats[cutoff:]])
        return train,test


    def implementMethods(self,sents,labelsData,clsent):
        labelwords=[]
        k=0

        
        cl=self.featureList(sents,labelsData)
        tr,te=self.setSplit(cl)
        nb_classifier = NaiveBayesClassifier.train(tr)
        print('Accuracy = '+str(accuracy(nb_classifier, te)*100)+'%')
        return nb_classifier
        
