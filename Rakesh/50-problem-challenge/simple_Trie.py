__author__ = 'rakesh'

#trie using dictionary of dictionary

words = ['rakesh', 'ranjan', 'raku', 'rammm', 'ramdev', 'rahjan']


def trie(words):
    _end = '_end'
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

print trie(words)














