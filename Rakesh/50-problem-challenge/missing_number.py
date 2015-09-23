__author__ = 'rakesh'


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=2:
            return None  #for missing number the length should be greater than 3
        storeList = dict()
        #the way the question is constructed, I am assuming the difference between a[1]-a[0]
        commonDifference = nums[1] - nums[0]
        for i in nums:
            storeList[i] = ''
        for j in range(len(nums)-1):
            if storeList.has_key(nums[j]+commonDifference):
                pass
            else:
                return nums[j] + commonDifference

#solve it using xor method if your array is fixed
#simple XOR will solve your problem
#definately solve it using XOR









