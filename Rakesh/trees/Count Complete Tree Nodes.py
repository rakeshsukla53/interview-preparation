# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ''' For complete binary tree the number of nodes = 2^height of tree - 1'''

    def totalNodes(self, root):

        if root is None:
            return 0
        else:
            return 1 + self.totalNodes(root.left) + self.totalNodes(root.right)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        height = self.totalNodes(root)

        print height

       
