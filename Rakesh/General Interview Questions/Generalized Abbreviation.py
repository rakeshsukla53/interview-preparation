
from itertools import permutations, combinations

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        for i in combinations(word, 4):
            print i





Solution().generateAbbreviations('word')
