__author__ = 'rakesh'

#follow this links for more information
# This is a dictionary whose keys are the nodes of the graph. For each key, the corresponding value is a list containing the nodes that are connected by a direct arc from this node. This is about as simple as it gets (even simpler, the nodes could be represented by numbers instead of names, but names are more convenient and can easily be made to carry more information, such as city names).
#
# Let's write a simple function to determine a path between two nodes. It takes a graph and the start and end nodes as arguments. It will return a list of nodes (including the start and end nodes) comprising the path. When no path can be found, it returns None. The same node will not occur more than once on the path returned (i.e. it won't contain cycles). The algorithm uses an important technique called backtracking: it tries each possibility in turn until it finds a solution.

graph = {'A': ['B', 'C', 'K'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C'],
             'K': ['S'],
             'S': ['L', 'P', 'D'],
             'P': ['Z']}

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                '''
                there is a difference between using return and assign a variable to function.
                1- if we use return then the final result will be returned back and there will save of previous value
                2- return is like going deep in to the tree and returning something to print but if you need to add or perform some operation during in the recursion then you need to save its state.
                3- here they have used newpath to save the previous state
                4- then here we have used if newpath which shows that if there is any value returned other than None, then return to the main function.
                5- There are multiple ways to use the recurison

                find_path(graph, node, end, path) #just keeping on looping without saving anything
                But with recursion you should have a base condition and factor which keep on decreasing and equal to the base condition

                return find_path(graph, node, end, path)

                Here whatever will be output will be returned back

                newpath = find_path(graph, node, end, path)

                Finding the output and savings its state.

                This is a perfect example on how to use recursion
                '''
                if newpath: return  newpath
        return None

print find_path(graph, 'A', 'Z')


