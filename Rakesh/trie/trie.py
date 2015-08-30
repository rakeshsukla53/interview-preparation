from pytrie import SortedStringTrie as trie

t = trie(an=0, ant=1, all=2, allot=3, alloy=4, aloe=5, are=6, be=7)

print t

'''
A trie is an tree data structure that is used to store a mapping where the keys are sequences, usually strings over an alphabet. In addition to implementing the mapping interface, tries facilitate finding the items for a given prefix, and vice versa, finding the items whose keys are prefixes of a given key K. As a common special case, finding the longest-prefix item is also supported.
'''

'''
Algorithmically, tries are more efficient than binary search trees (BSTs) both in lookup time and memory when they contain many keys sharing relatively few prefixes. Unlike hash tables, trie keys don’t need to be hashable.
'''

#Trie data strcuture https://reterwebber.wordpress.com/2014/01/22/data-structure-in-python-trie/
# >>> from pytrie import SortedStringTrie as trie
# >>> t = trie(an=0, ant=1, all=2, allot=3, alloy=4, aloe=5, are=6, be=7)
# >>> t
# {'all': 2, 'allot': 3, 'alloy': 4, 'aloe': 5, 'an': 0, 'ant': 1, 'are': 6, 'be': 7}
# >>> t.keys(prefix='al')
# ['all', 'allot', 'alloy', 'aloe']
# >>> t.items(prefix='an')
# [('an', 0), ('ant', 1)]
# >>> t.longest_prefix('antonym')
# 'ant'
# >>> t.longest_prefix_item('allstar')
# ('all', 2)
# >>> t.longest_prefix_value('area', default='N/A')
# 6
# >>> t.longest_prefix('alsa')
# Traceback (most recent call last):
#     ...
# KeyError
# >>> t.longest_prefix_value('alsa', default=-1)
# -1
# >>> list(t.iter_prefixes('allotment'))
# ['all', 'allot']
# >>> list(t.iter_prefix_items('antonym'))
# [('an', 0), ('ant', 1)]