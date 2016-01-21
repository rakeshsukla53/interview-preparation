
from pytrie import SortedStringTrie as trie

t = trie(an=0, ant=1, all=2, allot=3, alloy=4, aloe=5, are=6, be=7)

print t

print t.keys(prefix='al')

print t.items(prefix='an')

print t.longest_prefix('antonym')

print t.longest_prefix_value('alsa', default=-1)

print list(t.iter_prefixes('allotment'))

print list(t.iter_prefix_items('antonym'))






