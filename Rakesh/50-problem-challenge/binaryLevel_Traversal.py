__author__ = 'rakesh'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Such questions will always be solved using a deque or queue. Breadth for search is solved using these concepts
'''
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None

        result = []
        d = deque()
        d.append(root)
        while len(d) != 0:
            if d[0].left != None:
                d.append(d[0].left)
            if d[0].right != None:
                d.append([d[0].right])
            result.append(d.popleft().val)

