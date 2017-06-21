from wordSeperator import *
import glob
import os


class invertedIndex:

    def __init__(self,invertedIndex,fileSum=3):
        self.ini=invertedIndex
        self.wordSeperator=wordSeperator()
        self.fileSum=fileSum

    def boolAnd(self,first,second,notOne,notTwo):
        try:
            if notOne and notTwo:
                return self.boolNot(self.boolOr(first, second))
            joinedWordList = []
            if notOne:
                joinedWordList=self.wordSeperator.not_And(first,second)
            elif notTwo:
                joinedWordList=self.wordSeperator.not_And(second,first)
            else:
                joinedWordList=self.wordSeperator.And(first,second)
            return joinedWordList
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E

    def boolOr(self,first,second,notOne,notTwo):
        try:
            if notOne and notTwo:
                return self.boolNot(self.boolAnd(first,second,0,0))
            if notOne:
                return self.wordSeperator.Or(self.boolNot(first),second)
            elif notTwo:
                return self.wordSeperator.Or(first,self.boolNot(second))
            else:
                return self.wordSeperator.Or(first,second)
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E

    def boolNot(self,first,fileSum):
        try:
            return self.wordSeperator.Not(first,fileSum)
        except Exception,E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E


    def boolSearch(self,ops):
        try:
            stackList=[]
            stackOp=[]
            rankOp={'AND':1,'OR':0,'NOT':2,'(':-1,')':-1}
            operator=['AND','OR','NOT','(',')']
            def calc():
                op=stackOp.pop()
                list1=stackList.pop()
                if op=='NOT':
                    return self.boolNot(list1,self.fileSum)
                else:
                    list2=stackList.pop()
                    if op=='OR':
                        return self.boolOr(list1,list2,0,0)
                    if op=='AND':
                        return self.boolAnd(list1,list2,0,0)
            for i in range(0,len(ops)):
                op=ops[i]
                if op in operator:
                    if stackOp:
                        if (op=='('):
                            stackOp.append(op)
                            continue
                        elif (op==')'):
                            while stackOp[-1]!='(':
                                stackList.append(calc())
                            stackOp.pop()
                            continue
                        elif rankOp[stackOp[-1]]<=rankOp[op]:
                            stackOp.append(op)
                        else:
                            while rankOp[stackOp[-1]]>rankOp[op]:
                                stackList.append(calc())
                            continue
                    else:
                       stackOp.append(op)
                else:
                    if self.ini.has_key(op):
                        stackList.append(self.ini[op])
                    else:
                        stackList.append([])
            while stackOp:
                    #print "done"
                    stackList.append(calc())
            return stackList[-1]
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E
