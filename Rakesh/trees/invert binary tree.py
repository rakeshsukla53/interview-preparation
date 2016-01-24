
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        if root.left != None:
            self.invertTree(root.left)
        if root.right != None:
            self.invertTree(root.right)

        return root

