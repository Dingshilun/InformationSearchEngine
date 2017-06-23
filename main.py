#!/usr/bin/env python
# coding: utf-8

import sys
import builder
import argparse
from invertedIndex import invertedIndex
from wordSeperator import singleList
import glob
from utility import wordProcess
import re

def train(fn):
    a=builder.indexBuilder()
    a.buildWordSet(fn)
    a.save()

def init():
    a=builder.indexBuilder()
    a.load()
    return a

def bool_main(fact, query,ini, fileName, disable_corrrector=False):
    if query:
        words = query
        words = words.replace('(', ' ( ')
        words = words.replace(')', ' ) ')
        words = words.split()

        if not disable_corrrector:
            words = [fact.corrector.correct(w) for w in words]
        res=ini.boolSearch(words)
        if res:
            result = ini.boolSearch(words)
            for item in result:
                print fact.filedict[item.fileNo]
            print '\033[1;35mTotal\033[0m:', len(result)
        else:
            print "nothing found"

    else:
        print 'Missing query keywords'

def vsm_main(fact, query, k, disable_corrrector=False):
    if query:
        words = wordProcess(query)
        if not disable_corrrector:
            words = [fact.corrector.correct(w) for w in words]
        qvector = fact.vsm.query_vector(words)
        result = fact.vsm.get_topK_list(qvector, k) if k and k > 0 else fact.vsm.get_sorted_scores_list(qvector)
        for item in result:
            print item[1], fact.filedict[item[0]]
        print '\033[1;35mTotal\033[0m:', len(result)
    else:
        print 'Missing query keywords'

def re_main(fact, query):
    result = set()
    for w in fact.wordSet:
        if re.findall(query, w):
            for i in xrange(len(fact.invertedIndex[w])):
                    result.add(fact.invertedIndex[w][i].fileNo)

    for item in result:
        print fact.filedict[item]
    print '\033[1;35mTotal\033[0m:', len(result)

def parse_main(argv):
    parser = argparse.ArgumentParser(description='Search Engine')
    parser.add_argument('-I', action='store_true', help='Interactive mode')
    parser.add_argument('-t', help='generate index and dictionary, "Reuters/*.html"')
    parser.add_argument('-q', help='query keys')
    parser.add_argument('-k', type=int, help='Top K')
    parser.add_argument('-V', '--vsm', action='store_true', default=True, help="default option")
    parser.add_argument('-B', '--bool', action='store_true')
    parser.add_argument('-R', '--regex', action='store_true')
    parser.add_argument('--disable_corrrector', action='store_true', default=False)

    args = parser.parse_args(argv)

    if not args.I:
        if args.t:
            train(args.t)
        else:
            indexFactory = init()
            ini=invertedIndex(indexFactory.invertedIndex,len(indexFactory.filedict))
            if args.bool:
                bool_main(indexFactory, args.q,ini,indexFactory.filedict, args.disable_corrrector)
            elif args.vsm:
                k = args.k if args.k else 0
                vsm_main(indexFactory, args.q, k, args.disable_corrrector)
            elif args.regex:
                re_main(indexFactory, query)
    else:
        indexFactory = init()
        ini=invertedIndex(indexFactory.invertedIndex,len(indexFactory.filedict))
        op = raw_input('operation: ')
        while not op == 'exit':
            query = raw_input('query words? ')

            if op == 'bool':
                bool_main(indexFactory, query,ini,indexFactory.filedict)
            elif op == 'vsm':
                k = int(raw_input('top K(0 to disable)? '))
                vsm_main(indexFactory, query, k)
            elif op == 'regex':
                re_main(indexFactory, query)

            op = raw_input('operation: ')

if __name__ == '__main__':
    parse_main(sys.argv[1:])
