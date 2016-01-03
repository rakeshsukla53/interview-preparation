

from collections import OrderedDict

class Solution(object):

    def topological_sorting(self, graph, root):
        state = set()

        def dfs(node):
            if node in state:
                raise ValueError('Cycle')
            else:
                state.add(node)
            for k in graph.get(node, []):
                dfs(k)
        dfs(root)
        return state

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = OrderedDict()

        for key, value in edges:
            if key in graph:
                graph[key].append(value)
            else:
                graph[key] = [value]
        root = graph.keys()[0]
        try:
            if len(self.topological_sorting(graph, root)) == n:
                return True
            else:
                return False
        except:
            return False

print Solution().validTree(5, [[0, 1], [1, 2], [3, 4]])

