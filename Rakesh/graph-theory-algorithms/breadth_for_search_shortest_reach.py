
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        if shortest is None:
            pass
        else:
            return shortest

from collections import defaultdict

test_cases = input()

for i in range(test_cases):
    graph = defaultdict(list)
    nodes = set()
    x, y = map(int, raw_input().strip().split())
    for j in range(y):
        b, c = raw_input().strip().split()
        nodes.add(b)
        nodes.add(c)
        graph[b] += [c]
        graph[c] += [b]
    starting_point = raw_input()
    for k in list(nodes):
        if k == starting_point:
            pass
        else:
            print (len(find_shortest_path(graph, starting_point, k))-1)*6,

    for _ in range(1, abs(y-x)):
                print -1

