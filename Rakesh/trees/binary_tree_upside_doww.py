__author__ = 'rakesh'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.count = 0

    def upsideDownBinaryTree(self, root, parent=None, count=0):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root.left != None:
                if count == 0:
                    node = BinarySearchTree(root.left.value)
                    right1 = BinarySearchTree(root.value)
                    left1 = BinarySearchTree(root.right.value)
                    node.right = right1
                    node.left = left1
                    count += 1
                    return self.upsideDownBinaryTree(root.left, node, count)
                else:
                    node = BinarySearchTree(root.left.value)
                    left1 = BinarySearchTree(root.right.value)
                    node.right = parent
                    node.left = left1
                    return self.upsideDownBinaryTree(root.left, node)

        return parent

#write iterative solution for this, and you can do it
#this is an recursive solution and this is how you have to write solution for tree
#this solution is wrong because by pointing the nodes to the left or right of tree, you are actually changing the behaviour of root also
#the concept is pretty same, and it is that you need to use iterative programming when you see a problem like this...