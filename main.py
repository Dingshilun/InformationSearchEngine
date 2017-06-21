from builder import *
import builder
import invertedIndex
from wordSeperator import singleList
import glob
def train():
    filepath="/Users/dingshilun/Documents/Senior/searchEngine/Reuters/*.html"
    a=builder.indexBuilder()
    a.buildWordSet(filepath)
    a.save()

def init():
    a=builder.indexBuilder()
    a.load()
    return a

ini=init()

index=invertedIndex.invertedIndex(ini)

#
# op=['a','OR','b','AND','c']
# res=index.boolSearch(op)
# for r in res:
#     print r.fileNo
# print
# op=['NOT','a']
# res=index.boolSearch(op)
# for r in res:
#     print r.fileNo
# print
#
# op=['a','AND','b','AND','c']
# res=index.boolSearch(op)
# for r in res:
#     print r.fileNo
# print
#
# op=['(','a','OR','b',')','AND','(','c','OR','b',')']
# res=index.boolSearch(op)
# for r in res:
#     print r.fileNo
# print
#
