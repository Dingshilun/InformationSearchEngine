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

    def sentenceSearch(self,first,second):
        try:
            p1=p2=0
            len1=len(first)
            len2=len(second)
            res=[]
            while p1<len1 and p2<len2:
                #if (first[p1].fileNo==1):
                 #   print "wait!"
                if (first[p1].fileNo==second[p2].fileNo):
                    l1=len(first[p1].shows)
                    l2=len(second[p2].shows)
                    pp1=pp2=0
                    newShows=[]
                    while pp1<l1 and pp2<l2:
                        if (first[p1].shows[pp1]+1==second[p2].shows[pp2]):
                            newShows.append(second[p2].shows[pp2])
                            pp1=pp1+1
                            pp2=pp2+1
                        elif (first[p1].shows[pp1]<second[p2].shows[pp2]):
                            pp1=pp1+1
                        elif (first[p1].shows[pp1]>second[p2].shows[pp2]):
                            pp2=pp2+1
                    newSingleList=singleList(first[p1].fileNo,newShows)
                    res.append(newSingleList)
                    p1=p1+1
                    p2=p2+1
                elif (first[p1].fileNo<second[p2].fileNo):
                    p1=p1+1
                elif (first[p1].fileNo>second[p2].fileNo):
                    p2=p2+1
            #print res
            return res
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E
    def boolSearch(self,ops):
       # try:
       stackList = []
       stackOp = []
       rankOp = {'AND': 1, 'OR': 0, 'NOT': 2, '(': -1, ')': -1}
       operator = ['AND', 'OR', 'NOT', '(', ')']
       #print self.fileSum

       def calc(self):
           op = stackOp.pop()
           list1 = stackList.pop()
           #print op, list1[0].fileNo
           if op == 'NOT':
               return self.boolNot(list1, self.fileSum)
           else:
               list2 = stackList.pop()
               if op == 'OR':
                   return self.boolOr(list1, list2, 0, 0)
               if op == 'AND':
                   return self.boolAnd(list1, list2, 0, 0)

       for i in range(0, len(ops)):
           op = ops[i]
           #print op, i
           if op in operator:
               if stackOp:
                   if (op == '('):
                       stackOp.append(op)
                       continue
                   elif (op == ')'):
                       while stackOp[-1] != '(':
                           stackList.append(calc(self))
                       stackOp.pop()
                       continue
                   elif rankOp[stackOp[-1]] <= rankOp[op]:
                       stackOp.append(op)
                   else:
                       while stackOp and rankOp[stackOp[-1]] > rankOp[op]:
                           stackList.append(calc(self))
                           # print "done", len(stackList[-1])
                       continue
               else:
                   stackOp.append(op)
           else:
               if self.ini.has_key(op):
                   if (stackList and ops[i - 1] not in operator):
                       stackList.append(self.sentenceSearch(stackList.pop(), self.ini[op]))
                   else:
                       stackList.append(self.ini[op])
               else:
                   if (stackList and ops[i - 1] not in operator):
                       stackList.pop()
                   stackList.append([])
       while stackOp:
           # print "done"
           stackList.append(calc(self))
       return stackList[-1]
       # except Exception, E:
        #    print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E
