
# class Solution(object):
#     def countSmaller(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """

import bisect
nums = [5, 2, 1, 1]

print bisect.bisect_left(nums, 5, 1, 4)
