# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.tree_nodes = []

    def depthForSearch(self, root):
        if root.left:
            self.depthForSearch(root.left)
        else:
            self.tree_nodes.append(2)
        self.tree_nodes.append(root.val)
        if root.right:
            self.depthForSearch(root.right)
        else:
            self.tree_nodes.append(3)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        self.depthForSearch(p)
        first_tree = list(self.tree_nodes)
        print first_tree
        self.tree_nodes = []
        self.depthForSearch(q)
        second_tree = list(self.tree_nodes)
        print second_tree

        if first_tree == second_tree:
            return True
        return False



