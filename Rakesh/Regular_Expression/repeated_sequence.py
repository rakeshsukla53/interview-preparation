
# start optimizing now
from collections import defaultdict

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        # if length < 10:
        #     return []
        #
        # return [s[i: i + 10] for i in range(length) if not s.find(s[i: i + 10], i + 10, -1) == -1]
        # it will occupy lot of memory
        result = defaultdict()
        for i in range(length - 10):
            sub_string = s[i:i+10]
            if sub_string in result:
                result[sub_string] += 1
            else:
                result[sub_string] = 1
        return [item for item in result if result[item] > 1]

print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

