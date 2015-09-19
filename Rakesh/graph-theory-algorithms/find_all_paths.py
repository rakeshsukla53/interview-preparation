__author__ = 'rakesh'

graph = {'A': ['B'],
             'B': ['C'],
             'C': ['D', 'F']}


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

print find_path(graph, 'A', 'D')
