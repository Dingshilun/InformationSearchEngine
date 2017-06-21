from builder import *
import builder

def train():
    filepath="/Users/dingshilun/Documents/Senior/searchEngine/Reuters/*.html"
    a=builder.indexBuilder()
    a.buildWordSet(filepath)
    a.save()

def init():
    a=builder.indexBuilder()
    a.load()