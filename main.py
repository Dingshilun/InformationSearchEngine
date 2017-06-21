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

train()

# ini=init()
# files=glob.glob("/Users/dingshilun/Documents/Senior/searchEngine/Reuters/*.html")
# index=invertedIndex.invertedIndex(ini.invertedIndex)
#
# a=ini.invertedIndex['review']
# for item in a:
#     print item.fileNo,len(item.shows),
# print
#
# op=['bahia','cocoa','review']
# res=index.boolSearch(op)
# for r in res:
#    print files[r.fileNo-1],
# print
# op=['bahia','AND','cocoa','AND','review']
# res=index.boolSearch(op)
# for r in res:
#     print files[r.fileNo-1],
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

