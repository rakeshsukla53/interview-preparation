
class Solution(object):
    def rotate(self, nums, k):
        """
        Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0

        while i < k:
            nums.insert(0, nums.pop())
            i += 1

Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)

class Solution(object):
    def rotate(self, nums, k):
        """
        Rotate an array of n elements to the right by k steps.

        For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        # this is how you do in place shift
