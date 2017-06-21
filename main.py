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

def bool_main(fact, query):
    if query:
        words = query
        words = words.replace('(', ' ( ')
        words = words.replace(')', ' ) ')
        words = words.split()
        print words
    else:
        print 'Missing query keywords'

def phrase_main(fact, query):
    if query:
        words = query.split()
        print words
    else:
        print 'Missing query keywords'

def vsm_main(fact, query, k):
    if query:
        words = query.split()
        ## process word
        # qvector = fact.vsm.query_vector(words)
        # if k and k > 0:
        #     fact.vsm.get_topK_list(qvector, k)
        # else:
        #     fact.vsm.get_sorted_scores_list(qvector)
    else:
        print 'Missing query keywords'

def parse_main(argv):
    parser = argparse.ArgumentParser(description='Search Engine')
    parser.add_argument('-I', action='store_true', help='Interactive mode')
    parser.add_argument('-t', help='generate index and dictionary, "Reuters/*.html"')
    parser.add_argument('-q', help='query keys')
    parser.add_argument('-k', type=int, help='Top K')
    parser.add_argument('-V', '--vsm', action='store_true', default=True, help="default option")
    parser.add_argument('-B', '--bool', action='store_true')
    parser.add_argument('-P', '--phrase', action='store_true')
    parser.add_argument('--disable_corrrector', action='store_true')

    args = parser.parse_args(argv)

    if not args.I:
        if args.t:
            train(args.t)
        else:
            indexFactory = init()
            print len(indexFactory.wordSet)
            if args.bool:
                bool_main(indexFactory, args.q)
            elif args.phrase:
                phrase_main(indexFactory, args.q)
            elif args.vsm:
                vsm_main(indexFactory, args.q, k)
    else:
        indexFactory = init()
        op = raw_input('operation: ')
        while not op == 'exit':
            tp = raw_input('searching type? ')
            query = raw_input('query words? ')

            if tp == 'bool':
                bool_main(indexFactory, query)
            elif tp == 'phrase':
                phrase_main(indexFactory, query)
            elif tp == 'vsm':
                k = raw_input('top K(0 to disable)? ')
                vsm_main(indexFactory, query, k)

            op = raw_input('operation: ')

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
