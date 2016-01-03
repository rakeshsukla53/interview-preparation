
# the basics of 3 pointer and how it can be implemented in questions like these
# this question is also known as 3SUM Algorithm

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 2):
            a = nums[i]
            # this is the concept of two pointers. One will start from i + 1, and other from n - 1
            start = i + 1
            # end will start from n - 1
            end = n - 1
            # the process will go on till start and end are equal
            while start < end:
                # take the next value of b and c
                b = nums[start]
                c = nums[end]
                # if the sum is less than target, then capture the value
                if a + b + c < target:
                    count += end - start
                    start += 1
                else:
                    end -= 1

                    # if you need to decrease the value of end here anyway since you're checking for all the values less than target.

        # return the final count or you can just yield it
        return count

print Solution().threeSumSmaller([3, 1, 0, -2], 4)

# if you want to check the value of zero then you need can insert all the values into a hash table

