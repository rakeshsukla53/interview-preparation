# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """



def rootToLeaf(self, paths=[]):
        paths = paths + [str(self.value)]
        if self.left == None and self.right == None:
            return paths
        if self.left != None:
            newpath = self.left.rootToLeaf(paths)
            if newpath:
                print "->".join(newpath)
        if self.right != None:
            oldpath = self.right.rootToLeaf(paths)
            if oldpath:
                print "->".join(oldpath)
