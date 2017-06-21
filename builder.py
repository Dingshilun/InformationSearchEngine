
from utility import *
from wordSeperator import wordSeperator
import glob
import cPickle
class indexBuilder:
    def __init__(self):
        pass

    def buildWordSet(self,filepath):
        wordSet=set('')
        wordDict={}
        count=0
        invertedIndex={}
        self.seperator=wordSeperator()
        files=glob.glob(filepath)
        files.sort()
        for file in files:
            print file
            trainingFile=open(file,'r')
            fileDict={}
            fileString=""
            while True:
                words=trainingFile.readline()
                if not words:
                    break
                fileString=fileString+words
                word=wordProcess(words)
                for w in word:
                    if not (w in stopset or w in deleteset):
                        wordSet.add(w)
                        if not fileDict.has_key(w):
                            fileDict[w]=1
                        else:
                            fileDict[w]=fileDict[w]+1
            for key in wordDict:
                if (fileDict.has_key(key)):
                    wordDict[key].append(fileDict[key])
                else:
                    wordDict[key].append(0)
            for key in fileDict:
                if not (wordDict.has_key(key)):
                    wordDict[key]=[]
                    for i in range(0,count-1):
                        wordDict[key].append(0)
                    wordDict[key].append(fileDict[key])
            invertedDict=self.seperator.Splite(fileString,count)
            #print invertedDict
            for key in invertedDict:
                if invertedIndex.has_key(key):
                    invertedIndex[key].append(invertedDict[key])
                else:
                    invertedIndex[key]=[]
                    invertedIndex[key].append(invertedDict[key])
            count = count + 1
        self.wordSet=wordSet
        self.wordDict=wordDict
        self.invertedIndex=invertedIndex

    def getInvertedIndex(self):
        return self.invertedIndex
    def getWordSet(self):
        return self.wordSet
    def getWordDict(self):
        return self.wordDict

    def save(self):
        output=open("invertedIndex.pkl",'wb')
        cPickle.dump(self.invertedIndex,output,2)
        output=open("wordSet.pkl",'wb')
        cPickle.dump(self.wordSet,output,2)
        output=open("wordDict.pkl",'wb')
        cPickle.dump(self.wordDict,output,2)
    def load(self):
        input=open('invertedIndex.pkl','rb')
        self.invertedIndex=cPickle.load(input)
        input=open("wordSet.pkl",'rb')
        self.wordSet=cPickle.load(input)
        #input=open("wordDict.pkl",'rb')
        #self.wordDict=cPickle.load(input)
