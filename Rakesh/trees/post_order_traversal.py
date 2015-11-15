# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.result = []

    def postOrder(self, root):

        if root.left:
            self.postOrder(root.left)
        if root.right:
            self.postOrder(root.right)
        self.result.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.postOrder(root)
        return self.result
