__author__ = 'rakesh'


valueMapping = { '1' : ['2', '3', '4', '5', '6', '7', '8']}


def find_all_subsets(graph, start, path=[]):
        path = path +  [start]  # there is a huge difference between path += [start] and path = path + [start]. Former one is appending and alter one is just adding or arithemic addition
        if len(path) == 2:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node:
                newpaths = find_all_subsets(graph, node, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

print find_all_subsets(valueMapping, '1')

