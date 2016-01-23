class Solution(object):

    # creating sum of nums for quick query

    def sum_range(self, nums, i, j):

        if not i:
            return nums[j]
        else:
            return nums[j] - nums[i - 1]

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # this sum is equivalent to range sum query immutable
        # this is absolutely brilliant idea, using the hash table

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]


# well you are here trying to bypass some weak test cases, but eventually the worst case complexity is O(n*n)

