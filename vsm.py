#!/usr/bin/env python
# coding: utf-8

from __future__ import division

import math
import heapq
import numpy as np

class VSM:
    def __init__(self, dicts):
        # dicts.items ([tfs])
        self.term_count = len(dicts)
        self.doc_count = len(dicts.values()[0])
        self.dicts = dicts

        # Matrix: t x d
        self.tfidf = np.zeros((self.term_count, self.doc_count))
        idx = 0
        for t in self.dicts.itervalues():
            idf = math.log10(self.doc_count / (self.doc_count - t.count(0)))
            tfs = np.array([(1 + math.log10(i)) if i > 0 else 0 for i in t])
            self.tfidf[idx] = tfs * idf
            # self.tfidf[idx] = tfs
            idx += 1

        # normalize tfidf
        for x in xrange(self.doc_count):
            self.tfidf[:,x] = self._normalize(self.tfidf[:,x])

    def query_vector(self, query):
        vec = np.zeros(self.term_count)
        for k in query:
            if self.dicts.has_key(k):
                vec[self.dicts.keys().index(k)] += 1

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
