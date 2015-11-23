
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
                # keep adding since the sum is smaller
                continue
            else:
                while total_sum >= s:
                    # since we are talking about continuous array this technique will work
                    if len(subarray) < min_length:
                        # if you found a smaller length subarray then take that value
                        min_length = len(subarray)
                    total_sum -= subarray.popleft()

        if min_length == sys.maxint:
            return 0
        else:
            return min_length

print Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])

