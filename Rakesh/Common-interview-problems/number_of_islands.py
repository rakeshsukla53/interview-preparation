__author__ = 'rakesh'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __int__(self):
        self.validBinaryTree = []

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left != None:
            root.isValidBST(root.left)
        self.validBinaryTree.append(root.val)
        if root.right != None:
            root.isValidBST(root.right)

        if len(self.validBinaryTree) < 2:
            return False

        for i in range(len(self.validBinaryTree)-1):
            if self.validBinaryTree[i] > self.validBinaryTree[i+1]:
                return False

        return True

#the logic of inorder traversal should be in a different function. First you are calling so many times and then you are using the same function
#WRONG WRONG Always define a new function for anything
#List are mutable so they are adding new values then don't worry

