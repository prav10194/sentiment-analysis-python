#Lemmatization and Word Tagging

from nltk.tag import UnigramTagger,BigramTagger,TrigramTagger
from nltk.tokenize import word_tokenize
from multipleTagging import tagging
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import treebank

class TaggingAndLemmatize:

    def tagMap(self,treebank_tag):
        if treebank_tag==None:
            return wordnet.NOUN
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
    
    def LemmatizeSents(self,sents):
        tagger=tagging(treebank.tagged_sents(),[UnigramTagger,BigramTagger,TrigramTagger],backoff=None)
        newSents=[]
        for sent in sents:
            taggedSent=tagger.tag(word_tokenize(sent))
            words=[]
            for (wd,tg) in taggedSent:
                newTag=self.tagMap(tg)
                wd=WordNetLemmatizer().lemmatize(wd,newTag)
                words=words+[wd]
            newSent=' '.join(words)
            #print(newSent)
            newSents.append(newSent)
        return newSents
