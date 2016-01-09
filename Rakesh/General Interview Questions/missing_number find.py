
# Given nums = [0, 1, 3] return 2.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1 and not nums[0] == 1:
            return nums[0] + 1
        elif len(nums) == 1 and nums[0] == 1:
            return 0

        for i in range(1, len(nums)):
            if not nums[i] - 1 == nums[i - 1]:
                return nums[i - 1] + 1

        return nums[i] + 1

print Solution().missingNumber([0, 1])

