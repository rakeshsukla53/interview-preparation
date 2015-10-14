__author__ = 'rakesh'

graph = {'1': ['2', '3'],
         '2': ['3'],
         '3': ['']
         }

def find_all_paths(graph, start, path=[]):
        path = path + [start]
        if len(path) == 2:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node:
                newpaths = find_all_paths(graph, node, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

print (find_all_paths(graph, '1'))

#this is also the base of your maze program

# here the values will be your front and down value.
#graph[start] will consists of two values front and down and then you will iterative over it
#if a good solution is not found then it will return back to before loop

