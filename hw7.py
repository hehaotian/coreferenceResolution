# -*- coding: utf-8 -*-
"""
LING571 HW7

Created on Thu Mar 18 17:25:09 2014

@author: haotianhe
"""

import nltk
import pprint
import sys

def printfunc(sent_pair):

    tree_1 = parser.nbest_parse(sent_pair[0], 1)
    tree_2 = parser.nbest_parse(sent_pair[1], 1)

    s_1 = nltk.tree.ParentedTree.convert(tree_1[0])
    s_2 = nltk.tree.ParentedTree.convert(tree_2[0])

    pron = get_pron(str(s_2))
    proposed_nodes = []
    case = None
    for x in s_1.subtrees():
        cur = x.node.__repr__()[:2]            
        if cur == 'S[':
            proposed_nodes.append((x,case))
        elif cur == 'NP':
            parent = x.parent().node.__repr__()[:2]                
            if parent == 'VP':
                case= 'acc'               
            proposed_nodes.append((x,case))

    print "i) " + pron + s_1.pprint(margin=500) + s_2.pprint(margin=500)
    print "A) " + s_1.pprint(margin=500) 
    print "A) " + s_2.pprint(margin=500)
    proposed_print(proposed_nodes)
    print ""

def get_pron(s):
    tokens = s.split(' ')
    for i in range(len(tokens)):
        if "(PRP[]" in tokens[i]:
            pron = tokens[i + 1]
            break
    return pron[:-3]

def proposed_print(proposed_nodes):
    for proposed_node in proposed_nodes:
        if proposed_node[1] != 'acc':
            print "B) " + proposed_node[0].pprint(margin=500)

if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        grammar = nltk.data.load("file:" + sys.argv[1])
        sentences = open(sys.argv[2], 'r')
    else:
        grammar = nltk.data.load("file:grammar.fcfg")
        sentences = open("coref_sentences.txt", 'r')

    parser = nltk.parse.FeatureEarleyChartParser(grammar)

    sent_num = 0
    sent_pair = []
    for sent in sentences:
        sent_num += 1
        sent = nltk.tokenize.wordpunct_tokenize(sent)
        sent_pair.append(sent)
        if sent_num % 3 == 0:
            printfunc(sent_pair)
            sent_pair = []

    sentences.close()