from wordSeperator import *
import glob
import os


class buildInvertedIndex:

    def __init__(self,invertedIndex):
        self.ini=invertedIndex

    def boolAnd(self,first,second,notOne,notTwo):
        try:
            if notOne and notTwo:
                return self.boolNot(self.boolOr(first, second))
            joinedWordList = []
            if notOne:
                joinedWordList=wordSeperator.not_And(first,second)
            elif notTwo:
                joinedWordList=wordSeperator.not_And(second,first)
            else:
                joinedWordList=wordSeperator.And(first,second)
            return joinedWordList
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E

    def boolOr(self,first,second,notOne,notTwo):
        try:
            if notOne and notTwo:
                return self.boolNot(self.boolAnd(first,second,0,0))
            if notOne:
                return wordSeperator.Or(self.boolNot(first),second)
            elif notTwo:
                return wordSeperator.Or(first,self.boolNot(second))
            else:
                return wordSeperator.Or(first,second)
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E

    def boolNot(self,first,fileSum):
        try:
            return wordSeperator.Not(first,fileSum)
        except Exception,E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E
    def boolSearch(self,):

