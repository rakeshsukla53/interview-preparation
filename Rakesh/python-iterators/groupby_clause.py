from itertools import groupby

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result = []
        for k, g in groupby(strings, key=len):
            result.append(sorted(list(g)))

        return result

print Solution().groupStrings(["ab", "ba", "d"])
