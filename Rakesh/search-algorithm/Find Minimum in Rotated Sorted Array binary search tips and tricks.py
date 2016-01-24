

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        first = 0
        last = len(nums) - 1

        # binary search algorithm always focus on the condition through which you can eliminate any half

        while first <= last:
            mid = (first + last) / 2
            if mid == last:
                return nums[mid]
            if mid == 0:
                return nums[mid] if nums[mid] < nums[mid + 1] else nums[mid + 1]

            # I can remove one half by this condition

            if nums[mid] < nums[last]:
                last = mid
            else:
                if nums[first] > nums[mid]:
                    first = mid + 1
                else:
                    if nums[first] > nums[last]:
                        first = mid + 1
                    else:
                        last = mid

print Solution().findMin([3, 2, 1, 0])

