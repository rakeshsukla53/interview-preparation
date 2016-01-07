
class Solution(object):

    def __init__(self):
        self.right = []
        self.left = []

    def left_root_inorder(self, root):
        if root.left is None:
            self.left.append(0)
        else:
            self.left_root_inorder(root.left)
        self.left.append(root.val)
        if root.right is None:
            self.left.append(0)
        else:
            self.left_root_inorder(root.right)

    def right_root_inorder(self, root):

        if root.right is None:
            self.right.append(0)
        else:
            self.right_root_inorder(root.right)
        self.right.append(root.val)
        if root.left is None:
            self.right.append(0)
        else:
            self.right_root_inorder(root.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (root.left is None and root.right is None):
            return True

        if root.left and root.right and (root.left.val == root.right.val):
            self.left_root_inorder(root.left)
            self.right_root_inorder(root.right)
        else:
            return False

        return self.left == self.right

