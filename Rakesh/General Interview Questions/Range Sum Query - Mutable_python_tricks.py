class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.old_nums = list(nums)
        self.nums = list(nums)

        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i - 1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.old_nums[i] = val
        for i in range(i, len(self.old_nums)):
            self.nums[i] = self.nums[i - 1] + self.old_nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not i:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i - 1]

# the whole solution can be combined into this

'''
class NumArray(object):
    def __init__(self, nums):
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j+1])
'''

