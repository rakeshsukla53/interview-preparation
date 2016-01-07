

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums

        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i - 1]

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

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)
print numArray.sumRange(0, 5)
print numArray.sumRange(2, 5)
print numArray.sumRange(0, 2)



# Your NumArray object will be instantiated and called as such:

