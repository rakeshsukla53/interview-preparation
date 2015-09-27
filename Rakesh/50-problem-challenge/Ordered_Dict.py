__author__ = 'rakesh'

#What is orderedDict
#An OrderedDict is a dict that remembers the order that keys were first inserted. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.

from collections import OrderedDict

LRUCache = OrderedDict()
count = 1
for i in [2, 4, 5, 6, 7, 9, 10]:
    LRUCache[i] = count
    count += 1

print LRUCache
LRUCache.popitem(last=False)
print LRUCache
# print LRUCache
#
# # del LRUCache[2]  #if you delete the old entry then you ened
# # LRUCache[2] = ""
# # print LRUCache
#
# #The best thing about orderedDict is that it remembers the order in which the keys are inserted. If the new entry overwrites and existing entry, the original insertion position will remain unchanged. Deleting an entry and reinseeting it will move to the end. This is really good for LRU Cache will deletes the entry
#
# #dictionary sorted by key
#
# LRUCache = sorted(LRUCache.items(), key= lambda t: t[1])
# print LRUCache  #It is really amazing that you can sort your LRUCache
#
# #there are lots of operation that you can perform
# # >>> # regular unsorted dictionary
# # >>> d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
# #
# # >>> # dictionary sorted by key
# # >>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# # OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
# #
# # >>> # dictionary sorted by value
# # >>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# # OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
# #
# # >>> # dictionary sorted by length of the key string
# # >>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
# # OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])
