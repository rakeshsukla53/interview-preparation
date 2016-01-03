
# this topic is extremely important

from collections import defaultdict
from collections import deque

class Solution(object):

    def topological_sorting(self, graph):
        topological_order, elements, state = deque(), set(graph), {}
        def dfs(node):
            state[node] = 'V' # V stands for visited
            for k in graph[node]:
                sk = state.get(k, None)
                if sk == 'V':
                    raise ValueError('Cycle') # if you are going back to same node then there is a cycle
                if sk == 'NV': # because this node is already been taken into account
                    continue
                elements.discard(k)
                dfs(k)
            topological_order.appendleft(node)
            state[node] = 'NV' # again restarting their state

        # purpose is the node from where we start, should be coming in traversing because that will be a cyclic. Once we are done traversing, we can again mark it `Not visited` since other node can point to the same node

        while elements:
            dfs(elements.pop())

        return len(topological_order)

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True

        graph = defaultdict(list)
        for key, value in prerequisites:
            graph[key].append(value)

        try:
            if self.topological_sorting(graph) <= numCourses:
                return True
            else:
                return False
        except:
            return False

print Solution().canFinish(1, [[1, 0]])

