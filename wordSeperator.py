import time;
import utility

class singleList:
    def __init__(self,fileNo,shows):
        self.fileNo=fileNo
        self.shows=shows
class wordSeperator:

    def __init__(self):
        pass
    def Splite(self,fileString,fileNo):
        try:
            all_text=fileString
            lowerWords=utility.wordProcess(all_text)
            dictionary={}
            address=0
            offset=0
            for lowerWord in lowerWords:
                if (lowerWord=='' or lowerWord in utility.deleteset or lowerWord in utility.stopset):
                    address=address+1
                    continue
                if not dictionary.has_key(lowerWord):
                    temp=singleList(fileNo,[address])
                    dictionary[lowerWord]=temp
                else:
                    dictionary[lowerWord].shows.append(address)
                offset=offset+len(lowerWord)
                address=address+1
            #print dictionary
            return dictionary
        except Exception,E:
            print time.strftime('%Y-%m-%d %H:%M:%S--',time.localtime(time.time())),Exception,":",E

    def joinWordLists(self,first,second):
        try:
            p1=p2=0
            len1=len(first)
            len2=len(second)
            joinedWordList=[]
            while True:
                if first[p1].fileNo>=second[p2].fileNo:
                    joinedWordList.append(second)
                    p2=p2+1
                else:
                    joinedWordList.append(first)
                    p1=p1+1
                if (p1>=len1):
                    joinedWordList=joinedWordList+second
                    break

        except Exception,E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E

    def Or(self,first,second):
        try:
            p1=p2=0
            joinedWordList=[]
            len1=len(first)
            len2=len(second)
            while p1<len1 and p2<len2:
                if (first[p1].fileNo==second[p2].fileNo):
                    joinedWordList.append(first[p1])
                    joinedWordList[-1].shows.append(list(second[p2].shows))
                    p1=p1+1
                    p2=p2+1
                elif(first[p1].fileNo<second[p2].fileNo):
                    joinedWordList.append(first[p1])
                    p1=p1+1
                elif(first[p1].fileNo>second[p2].fileNo):
                    joinedWordList.append(second[p2])
                    p2=p2+1
            while p1<len1:
                joinedWordList.append(first[p1])
                p1=p1+1
            while p2<len2:
                joinedWordList.append(second[p2])
                p2=p2+1
            return joinedWordList
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E

    def And(self,first,second):
        try:
            p1=p2=0
            joinedWordList=[]
            len1=len(first)
            len2=len(second)
            while p1<len1 and p2<len2:
                if (first[p1].fileNo==second[p2].fileNo):
                    joinedWordList.append(first[p1])
                    joinedWordList[-1].shows.append(second[p2].shows)
                    p1=p1+1
                    p2=p2+1
                elif first[p1].fileNo<second[p2].fileNo:
                    p1=p1+1
                elif first[p1].fileNo>second[p2].fileNo:
                    p2=p2+1
            return joinedWordList
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E

    def not_And(self, notfirst, second):
        try:
            joinedWordList = []
            len1 = len(notfirst)
            len2 = len(second)
            p1=p2=0
            while p1 < len1 and p2 < len2:
                if (notfirst[p1].fileNo < second[p2].fileNo):
                    p1 = p1 + 1
                elif (notfirst[p1].fileNo > second[p2].fileNo):
                    joinedWordList.append(second[p2])
                    p2 = p2 + 1
                elif (notfirst[p1].fileNo == second[p2].fileNo):
                    p1 = p1 + 1
                    p2 = p2 + 1
            while p2 < len2:
                joinedWordList.append(second[p2])
                p2 = p2 + 1
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E

    def Not(selfself,first,fileSum):
        try:
            joinedWordList=[]
            len1=len(first)
            p1=0
            for i in range(0,fileSum):
                if (p1<len1 and i==first[p1].fileNo):
                    p1=p1+1
                    continue
                else:
                    joinedWordList.append(singleList(i,[-1]))
            return joinedWordList
        except Exception, E:
            print time.strftime('%Y-%m-%d %H:%M:%S--', time.localtime(time.time())), Exception, ":", E
