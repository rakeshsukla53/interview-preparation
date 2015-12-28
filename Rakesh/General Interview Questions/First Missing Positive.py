
# Meaning of Constant Space

# Constant space means that the amount of space that your algorithm uses is independent of the input parameters. Say you are given an array of size n. If the amount of space your algorithm uses scales with n, then it's not constant. If your algorithm always uses a fixed amount of space (5 variables, an array of fixed size: 100, 300, 5000, etc..), you are golden.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        postive_array = filter(lambda x: x > 0, nums)
        if len(postive_array) == 0 or len(nums) == 0:
            return 1

        if len(postive_array) == 1:
            if postive_array[0] > 1:
                return postive_array[0] - 1
            else:
                return 2

        min_num = min(postive_array)
        max_num = max(postive_array)
        num_sum = sum(postive_array)

        if min_num == 1:
            n = max_num
            total_sum = (n * (n + 1)) / 2
            missing_number = total_sum - num_sum
            if missing_number == 0:
                missing_number = max_num + 1
        else:
            n = min_num - 1
            m = max_num
            inital_sum = (n * (n + 1)) / 2
            total_sum = (m * (m + 1)) / 2
            required_sum = total_sum - inital_sum
            missing_number = required_sum - num_sum
            if missing_number == 0:
                missing_number = min_num - 1

        return missing_number

# from the looks it seems like there is only one missing number in a continous list

print Solution().firstMissingPositive([1, 2, 3, 1000])

# there will be one more condition but consider it done!

# Another beautiful method is by
#
# If the datastructure can be mutated in place and supports random access then you can do it in O(N) time and O(1) additional space. Just go through the array sequentially and for every index write the value at the index to the index specified by value, recursively placing any value at that location to its place and throwing away values > N. Then go again through the array looking for the spot where value doesn't match the index - that's the smallest value not in the array. This results in at most 3N comparisons and only uses a few values worth of temporary space.







