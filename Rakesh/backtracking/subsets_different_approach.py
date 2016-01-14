

# Backtracking solution implemented through iteration no recursion

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 1:
            return None

        uniqueSubset = []
        nums.sort()
        
        for i in range(len(nums)):
            uniqueSubset.append([nums[i]])
        
            for j in range(len(uniqueSubset)):
        
                if i == len(nums) - 1:
                    break
                else:
        
                    uniqueSubset.append(uniqueSubset[j] + [nums[i + 1]])
        
        uniqueSubset.append([])

        return uniqueSubset


print Solution().subsets([1, 2, 3])


