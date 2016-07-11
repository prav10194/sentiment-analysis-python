#Implement NaiveBayesClassifier
import nltk
from nltk.classify import NaiveBayesClassifier
import collections
from nltk.classify.util import accuracy
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist

def wordDict(words):
    return dict([(w,True) for w in words])

def featureList(sents,labelsData,feature_detector=wordDict):
    featuresDict=collections.defaultdict(list)
    k=0
    #print(type(sents))
    #print(sents[0])
    for sent in sents:
        #print(type(sent))
        w=nltk.tokenize.word_tokenize(sent)
        #print(w)
        featuresDict[labelsData[k]].append(feature_detector(w))
        k=k+1
    return featuresDict

def setSplit(lf,split=0.75):
    train=[]
    test=[]
    for label,feats in lf.items():
            cutoff=int(len(feats)*split)
            train.extend([(feat,label) for feat in feats[:cutoff]])
            test.extend([(feat,label) for feat in feats[cutoff:]])
    return train,test

def high_information_words(labelled_words, score_fn=BigramAssocMeasures.chi_sq, min_score=5):
    word_fd = FreqDist()
    label_word_fd = ConditionalFreqDist()
    
    for label, words in labelled_words:
            for word in words:
                    word_fd[word] += 1
                    label_word_fd[label][word] += 1
        
    n_xx = label_word_fd.N()
    high_info_words = set()
    
    for label in label_word_fd.conditions():
            n_xi = label_word_fd[label].N()
            word_scores = collections.defaultdict(int)
            
            for word, n_ii in label_word_fd[label].items():
                    n_ix = word_fd[word]
                    score = score_fn(n_ii, (n_ix, n_xi), n_xx)
                    word_scores[word] = score
            
            bestwords = [word for word, score in word_scores.items() if score >= min_score]
            high_info_words |= set(bestwords)
    
    return high_info_words


def bag_of_words_in_set(words, goodwords):
    return wordDict(set(words) & set(goodwords))

def implementMethods(sents,labelsData,clsent):
    labelwords=[]
    k=0
    for sent in sents:
        labelwords.append((labelsData[k],nltk.tokenize.word_tokenize(sent)))
        k=k+1
    high_info_words=set(high_information_words(labelwords))
    feat_det=lambda words:bag_of_words_in_set(words,high_info_words)
    
    cl=featureList(sents,labelsData,feature_detector=feat_det)
    tr,te=setSplit(cl)
    nb_classifier = NaiveBayesClassifier.train(tr)
    print('Accuracy = '+str(accuracy(nb_classifier, te)*100)+'%')
    return nb_classifier
        
