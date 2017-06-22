
from utility import *
from wordSeperator import wordSeperator
import glob
import cPickle
from vsm import VSM
from corrector import Corrector

class indexBuilder:
    def __init__(self):
        pass

    def buildWordSet(self,filepath):
        wordSet=set('')
        count=0
        invertedIndex={}
        self.fileName={}
        self.seperator=wordSeperator()
        files=glob.glob(filepath)
        files.sort()
        for file in files:
            print file
            self.fileName[count]=file
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
        # self.wordDict=wordDict
        self.invertedIndex=invertedIndex

    def getInvertedIndex(self):
        return self.invertedIndex
    def getWordSet(self):
        return self.wordSet

    def save(self):
        output=open("invertedIndex.pkl",'wb')
        cPickle.dump(self.invertedIndex,output,2)
        output=open("wordSet.pkl",'wb')
        cPickle.dump(self.wordSet,output,2)
        output=open('fileName.pkl','wb')
        cPickle.dump(self.fileName,output,2)

    def load(self):
        print "reading index"
        input=open('invertedIndex.pkl','rb')
        self.invertedIndex=cPickle.load(input)
        print "reading wordSet"
        input=open("wordSet.pkl",'rb')
        self.wordSet=cPickle.load(input)
        print "reading dictionary"
        print "reading fileDictionary"
        input=open('fileName.pkl','rb')
        self.filedict=cPickle.load(input)

        print "loading vsm"
        self.vsm = VSM(self.invertedIndex, len(self.filedict))
        self.corrector = Corrector('trainer')
