
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.total_sum = 0

    def find_sum(self, root, paths=[]):
        # paths have to passed through a parameter otherwise it will not reverse back
        # simple depth for search for finding all the sums
        paths = paths + [str(root.val)]
        if root.left is None and root.right is None:
            # once you reach the leaf node, find the sum
            self.total_sum += int("".join(paths))
            return paths
        if root.left:
            # depth for search, move left
            self.find_sum(root.left, paths)
        if root.right:
            # now move right
            self.find_sum(root.right, paths)
        # this is a top down approach
        # we can also down bottom up but that will be get sum of all the digits
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.find_sum(root)
        return self.total_sum