
# for this method I am going to use the reverse binary tree method to check for symmetric tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.count = True

    def sym(self, L, R):

        if L is None and R is None:
            return True

        if L and R and L.val == R.val:
            self.sym(L.left, R.right)
            self.sym(L.right, R.left)
        else:
            self.count = False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (root.left is None and root.right is None):
            return True

        self.sym(root.left, root.right)
        return self.count

# optimized solution of symmetric tree

