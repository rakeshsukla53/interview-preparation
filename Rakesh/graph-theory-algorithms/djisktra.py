__author__ = 'rakesh'

from collections import defaultdict

n = input()

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: print newpath
        return None


for i in range(n):

    d = defaultdict(list)

    nodesEdges = raw_input().strip().split(" ")

    N = nodesEdges[0]
    M = nodesEdges[1]



    find_path()

