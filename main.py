#!/usr/bin/env python
# coding: utf-8

import sys
import builder
import argparse
from invertedIndex import invertedIndex
from wordSeperator import singleList
import glob
import utility

def train(fn):
    a=builder.indexBuilder()
    a.buildWordSet(fn)
    a.save()

def init():
    a=builder.indexBuilder()
    a.load()
    return a

def bool_main(fact, query,ini, fileName):
    if query:
        words = query
        words = words.replace('(', ' ( ')
        words = words.replace(')', ' ) ')
        words = words.split()
        for item in ini.boolSearch(words):
            print fileName[item.fileNo],
        print
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
        words = wordProcess(query)
        words = [fact.corrector.correct(i) for w in words]
        qvector = fact.vsm.query_vector(words)
        if k and k > 0:
            fact.vsm.get_topK_list(qvector, k)
        else:
            fact.vsm.get_sorted_scores_list(qvector)
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
            ini=invertedIndex(indexFactory.invertedIndex,len(indexFactory.filedict))
            print len(indexFactory.wordSet)
            if args.bool:
                bool_main(indexFactory, args.q,ini,indexFactory.filedict)
            elif args.phrase:
                phrase_main(indexFactory, args.q)
            elif args.vsm:
                vsm_main(indexFactory, args.q, k)
    else:
        indexFactory = init()
        ini=invertedIndex(indexFactory.invertedIndex,len(indexFactory.filedict))
        op = raw_input('operation: ')
        while not op == 'exit':
            tp = raw_input('searching type? ')
            query = raw_input('query words? ')

            if tp == 'bool':
                bool_main(indexFactory, query,ini,indexFactory.filedict)
            elif tp == 'phrase':
                phrase_main(indexFactory, query)
            elif tp == 'vsm':
                k = raw_input('top K(0 to disable)? ')
                vsm_main(indexFactory, query, k)

            op = raw_input('operation: ')

if __name__ == '__main__':
    parse_main(sys.argv[1:])
