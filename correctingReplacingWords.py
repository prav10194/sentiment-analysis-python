import re
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import time


class ExtractingData:


    def runMethods(self,sents):
        
        sents=self.removeApostrophes(sents)
        sents=self.removeHash(sents)
        sents=self.removeAtTheRate(sents)
        sents=self.removeLinks(sents)
        sents=self.removeStopwords(sents)
        sents=self.removeSpecialCharactersAndSpaces(sents)
        sents=self.removeExtraCharactersInWords(sents)
        
        return sents
        

    def removeHash(self,sents):
        newSents=[]
        for sent in sents:
            hashTags=re.findall('#[A-Za-z0-9]+',sent)
            hashedWordsToInclude=[]
            for word in hashTags:
                newWord=re.sub('#','',word)
                if wordnet.synsets(newWord):
                    sent=re.sub('#'+newWord,newWord,sent)
                else:
                    sent=re.sub('#'+newWord,'',sent)
            newSents.append(re.sub(r'(\s)+',' ',sent))
        
        return newSents


    def removeAtTheRate(self,sents):
        newSents=[]
        for sent in sents:
            sent=re.sub('@[A-Za-z0-9]+','',sent)
            newSents.append(re.sub(r'(\s)+',' ',sent))
  
        return newSents

    def removeLinks(self,sents):
        newSents=[]
        for sent in sents:
            sent=re.sub('(\w+:\/\/\S+)','',sent)
            newSents.append(re.sub(r'(\s)+',' ',sent))
    
        return newSents

    def removeStopwords(self,sents):
        st=stopwords.words('english')
        newSents=[]
        for sent in sents:
            wordSent=word_tokenize(sent)
            newWordSent=[w for w in wordSent if w not in st]
            newSents.append(' '.join(newWordSent))
     
        return newSents

    

    def removeExtraCharactersInWords(self,sents):
        newSents=[]
        for sent in sents:
            sent=re.sub('\.','',sent)
            for w in word_tokenize(sent):

                sent=re.sub(w,self.replace(w),sent)
            newSents.append(sent)
        return newSents


    def removeApostrophes(self,sents):

        a=[(r'won\'t', 'will not'),(r'can\'t', 'cannot'),(r'\'m', 'i am'),(r'ain\'t', 'is not'),(r'(\w+)\'ll', '\g<1> will'),(r'(\w+)n\'t', '\g<1> not'),(r'(\w+)\'ve', '\g<1> have'),(r'(\w+)\'s', '\g<1> is'),(r'(\w+)\'re', '\g<1> are'),(r'(\w+)\'d', '\g<1> would')]
        newSents=[]
        for sent in sents:
            for (n,m) in a:
                sent=re.sub(re.compile(n),m,sent)
            newSents.append(sent)
        return newSents

    def removeSpecialCharactersAndSpaces(self,sents):

        newSents=[]
        for sent in sents:
            sent=re.sub(r'[^A-Za-z0-9]',' ',sent)
            sent=re.sub(r'(\s)+',' ',sent)
            newSents.append(sent)
        return newSents
            
    def replace(self,word):   #Called by removeExtraCharactersInWords
        w=word
        if wordnet.synsets(w):
            return w
        newWord=re.sub(r'(\w*)(\w)\2(\w*)',r'\1\2\3',w)
        if newWord!=w:
            #print(s+'\t'+s1)
            return self.replace(newWord)   #return here is important

        else:
            return w

##    def progressReport(self,present,total):
##            print("Sentences read ("+str(present)+"/"+str(total)+")("+str(int(present/total*100))+"%)",end="\r")
##            time.sleep(0.01)


    

    


