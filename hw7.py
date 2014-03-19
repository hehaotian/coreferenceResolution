# -*- coding: utf-8 -*-
"""
LING571 HW7

Created on Thu Mar 18 17:25:09 2014

@author: haotianhe
"""

import nltk
import sys

if __name__ == "__main__":

    if (len(sys.argv) >= 2):
        grammar = nltk.data.load("file:" + sys.argv[1])
        sentences = open(sys.argv[2], 'r')
    else:
        grammar = nltk.data.load("file:grammar.cfg")
        sentences = open("coref_sentences.txt", 'r')

    parser = nltk.parse.FeatureEarleyChartParser(grammar)

    SentencePair = []

    for sent in sentences:
        if sent == "":
            continue

        sent = nltk.tokenize.wordpunct_tokenize(sent)
        SentencePair.append(sent)

        if len(SentencePair) == 2:
            sent_1 = parser.nbest_parse(SentencePair[0], 1)
            sent_2 = parser.nbest_parse(SentencePair[1], 1)
            if len(sent_1) == 1 and len(sent_2) == 1:
                treeToString = str(sent_1)
                print sent_1.pprint(margin=500) + '\n'
                print '\n'

    sentences.close()
