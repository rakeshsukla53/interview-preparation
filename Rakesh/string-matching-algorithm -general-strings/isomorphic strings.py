
from collections import defaultdict

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ismorphic_string = defaultdict()
        store_mapping = defaultdict()
        for letter1, letter2 in zip(s, t):
            if letter1 in ismorphic_string and not ismorphic_string[letter1] == letter2:
                return False
            elif letter1 not in ismorphic_string and letter2 in store_mapping:
                return False
            ismorphic_string[letter1] = letter2
            store_mapping[letter2] = ''
        return True

print Solution().isIsomorphic('foo', 'bar')


