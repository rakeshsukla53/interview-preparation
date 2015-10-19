__author__ = 'rakesh'

from collections import defaultdict


'''
searchTerms = ["a", "c", "d"]

d = defaultdict(list)

for i in searchTerms:
    for j in range(len(searchTerms)):
        d[j].append(i)


print d.items()
'''

d = dict()
a = ["a", "c", "d"]
for i in a:
    for j in range(len(a)):
        d.setdefault(j, []).append(i)


print d
