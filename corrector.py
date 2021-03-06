#!/usr/bin/env python
# coding: utf-8

import re, collections

class Corrector:
    def __init__(self, fn):
        text = re.findall('[a-z]+', file(fn).read().lower())
        self.NWORDS = self._train(text)
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def _train(self, features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

    def edits1(self, word):
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
        replaces = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
        inserts = [a + c + b for a, b in splits for c in self.alphabet]
        return set(deletes + transposes + replaces + inserts)

    def known_edits2(self, word):
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)

    def known(self, words):
        return set(w for w in words if w in self.NWORDS)

    def correct(self, word):
        if any(c.isdigit() for c in word) or (word in ['AND','NOT','OR','(',')']):
            return word

        candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word]
        ret = max(candidates, key=self.NWORDS.get)
        if word != ret:
            print '\033[1;35mCorrecting\033[0m: "%s" to "%s"'%(word, ret)

        return ret

if __name__ == '__main__':
    c = Corrector('trainer')
    print c.correct("sruprise")
