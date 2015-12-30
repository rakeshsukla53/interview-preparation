
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Logic :
        You will use two loops one going from left to right, and other from right to left
        for example if a = [1, 2, 3, 4]
        Going from left -> a = [1, 1, 2, 6]
        Going from right -> a = [24,12,8,6] here you will refer back to [1,2,3,4]
        The problem is the list will grow with the input array
        """
        size, temp = len(nums), 1
        output = [1] * size
        # left loop array
        for i in range(1, size):
            temp *= nums[i - 1]
            output[i] = temp
        temp = 1
        for j in range(size - 2, -1, -1):
            temp *= nums[j + 1]
            output[j] *= temp

        return output

# this slicing and merging of the arrays are O(n) operation

Solution().productExceptSelf([1, 2, 3, 4])

