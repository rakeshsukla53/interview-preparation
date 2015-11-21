
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

class Solution(object):

    def __init__(self):
        self.total_sum = 0

    def findMin(self, root, paths=[]):
        # paths has to be defined inside the function otherwise it will not reverse back
        ''' Find the mininum depth of a tree '''
        paths = paths + [str(root.val)]
        # depth for search for binary tree
        if root.left is None and root.right is None:
            # recursion breaking condition
            if len(paths) < self.min:
                self.min = len(paths)
            return paths
        if root.left:
            # move left of your tree
            self.findMin(root.left, paths)
        if root.right:
            # move right of your tree
            self.findMin(root.right, paths)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        self.findMin(root)
        return self.min
