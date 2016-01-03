
from collections import defaultdict
# hash table is a really bad idea for range queries. Try Binary Search Tree
# this idea is not going to work using Hash Table
# for range query, we should use Binary Search Tree

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        store_input = defaultdict(list)
        for index, value in enumerate(nums):
            store_input[value].append(index)

        for index, value in enumerate(nums):
            for t in xrange(t - 1, -1, -1):
                value_j = value - t
                if value_j in store_input:
                    for p in store_input[value_j]:
                        if index - p < k:
                            return True

        return False

Solution().containsNearbyAlmostDuplicate([0, 2147483647], 1, 2147483647)
