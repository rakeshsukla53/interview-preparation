__author__ = 'rakesh'

import sys

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def answer(root):
            if root == None:
                return 0
            else:
                left = answer(root.left)
                if left is False:
                    return False
                right = answer(root.right)
                if right is False:
                    return False
                value = 1 + max(left, right)
                difference = abs(left - right)
                if difference > 1:
                    return False
                return value
        result = answer(root)
        if result:
            return True
        return result

    