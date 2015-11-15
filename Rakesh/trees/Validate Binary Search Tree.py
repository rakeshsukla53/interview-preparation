
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # this function is called automatically by python
    def __init__(self):
        self.result = []

    def inOrder(self, root):

        if root.left:
            self.inOrder(root.left)
        self.result.append(root.val)
        if root.right:
            self.inOrder(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.inOrder(root)

        for i in range(len(self.result) - 1):
            if self.result[i] >= self.result[i + 1]:
                return False
        return True
