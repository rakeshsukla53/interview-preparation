__author__ = 'rakesh'

from collections import defaultdict

graph = defaultdict(list)

for i in range(10):

    x, y = raw_input().strip().split()
    graph[y] += [x]

print graph


