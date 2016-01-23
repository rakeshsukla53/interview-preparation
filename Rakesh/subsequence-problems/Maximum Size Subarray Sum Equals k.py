
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
        Args:
            nums (list): List of numbers
            k (int): sum value
        """
        if not nums:
            return 0

        maximum_size = 0
        for i in range(len(nums)):
            total_sum = 0
            for j in range(i, len(nums)):
                total_sum += nums[j]
                if total_sum == k:
                    if j - i > maximum_size:
                        maximum_size = j - i 
        return maximum_size + 1 if maximum_size else maximum_size
    
print Solution().maxSubArrayLen([-2, -1, 2, 1], 1)

# this solution will not pass simply because it is O(n2)

