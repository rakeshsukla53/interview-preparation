class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return reduce(lambda x, y: x ^ y, nums)

print Solution().singleNumber([1, 1, 2, 2, 3])
