#!/usr/bin/env python
# coding: utf-8

import sys
import builder
import argparse
import invertedIndex
from wordSeperator import singleList
import glob

def train(fn):
    a=builder.indexBuilder()
    a.buildWordSet(fn)
    a.save()

def init():
    a=builder.indexBuilder()
    a.load()
    return a

def parse_main(argv):
    parser = argparse.ArgumentParser(description='Search Engine')
    parser.add_argument('-t', help='generate index and dictionary')
    parser.add_argument('-q', help='query keys')
    parser.add_argument('-k', type=int, help='Top K')
    parser.add_argument('-V', '--vsm', action='store_true', default=True)
    parser.add_argument('-B', '--bool', action='store_true')
    parser.add_argument('-P', '--phrase', action='store_true')

    args = parser.parse_args(argv)

    if args.t:
        train(args.t)
    else:
        indexFactory = init()
        print len(indexFactory.wordSet)
        if args.bool:
            if args.q:
                words = args.q
                words = words.replace('(', ' ( ')
                words = words.replace(')', ' ) ')
                words = words.split()
                print words
            else:
                print 'Missing query keywords'

        elif args.phrase:
            if args.q:
                words = args.q.split()
                print words
            else:
                print 'Missing query keywords'

        elif args.vsm:
            if args.q:
                words = args.q.split()
                print words
            else:
                print 'Missing query keywords'

if __name__ == '__main__':
    parse_main(sys.argv[1:])

# ini=init()
#
# index=invertedIndex.invertedIndex(ini)
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
