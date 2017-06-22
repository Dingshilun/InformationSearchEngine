#!/usr/bin/env python
# coding: utf-8

from __future__ import division

import math
import heapq
import numpy as np

class VSM:
    def __init__(self, invertedIndex, doc_count):
        # dicts.items ([tfs])
        self.term_count = len(invertedIndex)
        self.dicts = invertedIndex.keys()

        # Matrix: t x d
        self.tfidf = np.zeros((self.term_count, doc_count))
        idx = 0
        for w in invertedIndex.iteritems():
            idf = math.log10(doc_count / len(w[1]))
            tfs = np.zeros(doc_count)
            for doc in w[1]:
                 tfs[doc.fileNo] = (1 + math.log10(len(doc.shows))) * idf

            self.tfidf[idx] = tfs
            idx += 1

        # normalize tfidf
        for x in xrange(doc_count):
            self.tfidf[:,x] = self._normalize(self.tfidf[:,x])

    def query_vector(self, query):
        vec = np.zeros(self.term_count)
        for k in query:
            if k in self.dicts:
                vec[self.dicts.index(k)] += 1

        # normalize query vector
        return self._normalize(vec)

    def get_scores(self, qvector):
        return np.dot(qvector, self.tfidf)

    def get_sorted_scores_list(self, qvector):
        vec = self.get_scores(qvector)
        res = [(i, vec[i]) for i in xrange(len(vec))]
        return sorted(res, reverse=True, key=lambda d: d[1])

    def get_topK_list(self, qvector, k):
        vec = self.get_scores(qvector)
        res = [(i, vec[i]) for i in xrange(len(vec))]
        return heapq.nlargest(k, res, key=lambda d: d[1])

    def _normalize(self, vec):
        dist = np.linalg.norm(vec)
        if dist > 0:
            vec /= dist
        return vec
