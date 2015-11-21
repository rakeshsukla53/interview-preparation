
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

def lowestCommonAncestor(self, p, q):
        '''Find the lowest common ancestor of two nodes'''

        if (p > self.value and q < self.value) or (p < self.value and q > self.value):
            return self.value  # that will be the root
        if p > self.value and q > self.value:
            return self.right.lowestCommonAncestor(p, q)
        if p < self.value and q < self.value:
            return self.left.lowestCommonAncestor(p, q)
        if p == self.value and (q > self.value or q < self.value):
            return p
        if q == self.value and (p > self.value or p < self.value):
            return q



