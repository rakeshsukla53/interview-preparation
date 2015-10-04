class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        finalOutput = []
        leftMaximum, rightMaximum = 0, 0
        if root.left == None and root.right == None:
            return root.val
        finalOutput.append(root.val)
        if root.left != None:
            if root.left.val <= 0:
                lowerLeftMaximum = self.findMaximumSum(root.left) + abs(root.left.val)
                if lowerLeftMaximum == 0:
                    pass
                else:
                    finalOutput.append(lowerLeftMaximum)
            leftMaximum = self.findMaximumSum(root.left)
            finalOutput.append(leftMaximum)

        if root.right != None:
            if root.right.val <= 0:
                lowerRightMaximum = self.findMaximumSum(root.right) + abs(root.right.val)
                if lowerRightMaximum == 0:
                    pass
                else:
                    finalOutput.append(lowerRightMaximum)
            rightMaximum = self.findMaximumSum(root.right)
            finalOutput.append(rightMaximum)

        finalOutput.append(root.val + rightMaximum + leftMaximum)
        finalOutput.append(root.val + leftMaximum)
        finalOutput.append(root.val + rightMaximum)
        print finalOutput
        return max(finalOutput)

    def findMaximumSum(self, root):
        if root == None:
            return 0
        else:
            return root.val + max(self.findMaximumSum(root.left), self.findMaximumSum(root.right))

#This sum factor works really well for positive numbers
#if the number is negative , we don't want to return it anyway so dont't worry about your function
