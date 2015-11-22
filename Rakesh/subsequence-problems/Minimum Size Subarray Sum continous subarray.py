
from collections import deque
import sys

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # if you are talking about continuous subarray then it will work
        # the complexity again is same is O(n^2)
        # there is no difference between two loops and one for loop and while loop

        subarray = deque()
        # this subarray will be used as window, we will popleft if the sum is more
        # we will append if the append if our sum is < sum

        min_length = sys.maxint
        total_sum = 0
        for i in nums:
            subarray.append(i)
            total_sum += i
            if total_sum < s:
                continue
            elif total_sum == s:
                # if you sum is equal then find out the length of the subarray
                if len(subarray) < min_length:
                    min_length = len(subarray)
            elif total_sum > s:
                while total_sum > s:
                    # pop out the left element if the sum is greater and then check for availability
                    total_sum -= subarray.popleft()
                    if total_sum == s:
                        if len(subarray) < min_length:
                            min_length = len(subarray)

        if min_length == sys.maxint:
            return 0
        else:
            return min_length

print Solution().minSubArrayLen(11, [1, 2, 3, 4, 4])

