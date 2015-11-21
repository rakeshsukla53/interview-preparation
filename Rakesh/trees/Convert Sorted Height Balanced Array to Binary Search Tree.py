

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        start = 0
        end = len(nums) - 1
        mid = start + end / 2
        if end >= start:
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[start:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
            return root
        else:
            return None

# convert a array into balanced binary search tree




