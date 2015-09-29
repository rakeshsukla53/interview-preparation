__author__ = 'rakesh'

#trie using dictionary of dictionary

words = ['rakesh', 'ranjan', 'raku', 'rammm', 'ramdev', 'rahjan']

from collections import defaultdict

def trie(words):
    _end = '_end'
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
            #The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.
    return root

print trie(words)














