__author__ = 'rakesh'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k, array=[]):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root.left is not None:
            self.kthSmallest(root.left, k)
        array.append(root.val)
        if len(array) == k:
            return array[-1]
        if root.right is not None:
            self.kthSmallest(root.right, k)

