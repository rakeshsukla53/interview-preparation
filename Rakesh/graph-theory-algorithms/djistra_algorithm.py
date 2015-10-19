#
from collections import defaultdict
import sys

d = defaultdict(list)

for i in range(7):
    inputValue = raw_input().strip().split(" ")
    inputValue = map(int, inputValue)  #converting the str value to int
    d[inputValue[0]].append((inputValue[1], inputValue[2]))
    if (inputValue[0], inputValue[2]) not in d[inputValue[1]]:
        d[inputValue[1]].append((inputValue[0], inputValue[2]))

def find_path(graph, start, end, path=[]):

        path = path + [start]
        if start == end:
            weight = 0
            for i in range(len(path)-1):
                for line in d[path[i]]:
                    if path[i+1] == line[0]:
                        weight += line[1]
            print weight
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node[0] not in path:
                newpath = find_path(graph, node[0], end, path)
                if newpath:
                    print newpath
        return None

find_path(d, 8, 6)





