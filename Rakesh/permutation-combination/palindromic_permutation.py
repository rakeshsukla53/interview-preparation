
from collections import Counter
from itertools import permutations

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        word_frequency = Counter(s)
        characters = word_frequency.keys()
        word_length = len(s)
        result = []
        if len(s) > 1 and len(word_frequency.keys()) == 1:
            return [s]
        if word_length % 2 != 0:
            if len(characters) == (word_length / 2) + 1:
                for s in characters:
                    if word_frequency[s] == 1:
                        del word_frequency[s]
                        break
                for i in permutations(word_frequency.keys(), len(word_frequency.keys())):
                    result.append("".join(list(i)) + s + "".join(list(i)[::-1]))

                return result
            else:
                return []
        else:
            if len(characters) == (word_length / 2):
                for i in permutations(word_frequency.keys(), len(word_frequency.keys())):
                    result.append("".join(list(i)) + "".join(list(i)[::-1]))

                return result
            else:
                return []

print Solution().generatePalindromes("aabbccc")
