# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        '''
        for breadth for search you have the use the deque but here only take the last value not all
        '''
        result = []
        finalResult, n = [], 0
        if root is None:
            return list()
        d = deque()
        d.append(root)
        result.append([root.val])
        while len(d) != 0:
            k = list(d)
            for node in k:
                if node.left != None:
                    finalResult.append(node.left.val)
                    d.append(node.left)
                if node.right != None:
                    finalResult.append(node.right.val)
                    d.append(node.right)
                d.popleft()
            result.append(finalResult)
            finalResult = []

        return map(lambda x: x[-1], result[:-1])

