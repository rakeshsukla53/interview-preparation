__author__ = 'rakesh'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        finalResult, n = [], 0
        if root is None:
            return list()
        d = deque()
        d.append(root)
        while len(d) != 0:
            if d[0] is None:
                finalResult.append(d.popleft())
            else:
                if d[0].left != None:
                    d.append(d[0].left)
                if d[0].right != None:
                    d.append(d[0].right)
                finalResult.append(d.popleft().val)
                if len(finalResult) == pow(2, n):
                    finalResult = filter(None, finalResult)
                    result.append(finalResult)
                    n += 1
                    finalResult =[]
        print result

#this condition will always be true for binary complete tree