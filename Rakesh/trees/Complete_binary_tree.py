
'''
Something about complete binary tree
compare the depth between left sub tree and right sub tree. A, If it is equal, it means the left sub tree is a full binary tree B, It it is not , it means the right sub tree is a full binary tree
'''

class Solution:
        # @param {TreeNode} root
        # @return {integer}
        def countNodes(self, root):
            if not root:
                return 0
            leftDepth = self.getDepth(root.left)
            rightDepth = self.getDepth(root.right)
            if leftDepth == rightDepth:
                return pow(2, leftDepth) + self.countNodes(root.right)
            else:
                return pow(2, rightDepth) + self.countNodes(root.left)

        def getDepth(self, root):
            if not root:
                return 0
            return 1 + self.getDepth(root.left)
