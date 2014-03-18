# -*- coding: utf-8 -*-
"""
LING571 HW7

Created on Thu Mar 18 17:25:09 2014

@author: haotianhe
"""

import nltk
import sys
import nltk.tokenize import RegexpTokenizer

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

        tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
        sent = tokenizer.tokenize(sent)
        SentencePair.append(nltk.wordpunct)

        if len(sent_pair) == 2:
            HobbsAlgorithms(sent_pair, parser)
            SentencePair = []

    sentences.close()


def HobbsAlgorithms(SentencePair, parser):
    sent_1 = parser.nbest_parse(SentencePair[0], 1)
    
