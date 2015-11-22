
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # consider to be done! there is nothing special here

        if root is None:
            return list()

        result = []
        # it will collect intermediate values
        final_result = []
        # it will collect all the nodes of a given level
        d = deque()
        # insert the first root into d, here d will collect all the tree node objects level wise
        d.append(root)
        # i will make sure which level to reverse
        i = 1
        # result is holding all the values of the level
        result.append([root.val])
        while len(d) != 0:
            # convert your deque into a list
            k = list(d)
            # iterate over the list and find all the values from it, append nodes to d and values to finalresult
            for node in k:
                if node.left:
                    final_result.append(node.left.val)
                    d.append(node.left)
                if node.right:
                    final_result.append(node.right.val)
                    d.append(node.right)
                # pop out the from deque once you iterate over it
                d.popleft()
            i += 1
            if i % 2 == 0:
                # append the reverse of level by level tree traversal
                result.append(final_result[::-1])
            else:
                # append the result
                result.append(final_result)
            # empty your final level nodes, and get ready to accept new nodes
            final_result = []

        return result[:-1]