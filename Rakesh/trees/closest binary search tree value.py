
# Definition for a binary tree node.

import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __int__(self):
        self.closet_value = [sys.maxint, 0]

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        if target > root.val:
            if target - root.val < self.closet_value[0]:
                self.closet_value[1] = root.val
            if root.right:
                return self.closestValue(root.right, target)

        elif target <= root.val:
            if root.val - target < self.closet_value[0]:
                self.closet_value[1] = root.val
            if root.left:
                return self.closestValue(root.left, target)

        return self.closet_value[1]
