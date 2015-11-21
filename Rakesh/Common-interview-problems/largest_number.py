
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted(nums, key=str, reverse=True)
        print nums

Solution().largestNumber([3, 30, 5, 9])





