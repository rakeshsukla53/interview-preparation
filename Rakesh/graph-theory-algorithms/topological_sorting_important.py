# In topological sorting you can have different sorting order

from collections import deque

def topological_sorting(graph):
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

    return topological_order

# cycle
graph1 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": []
}
try:
    print topological_sorting(graph1)
except:
    print 'Rakesh'



















