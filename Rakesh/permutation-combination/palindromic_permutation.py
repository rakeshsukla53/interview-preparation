
from collections import Counter
from itertools import permutations, repeat

class Solution(object):
    def generatePalindromes(self, s):
        """
        Generate all palindrome of a given sequence
        :type s: str
        :rtype: List[str]
        """
        # for not be palindrome we cannot have two character with frequency of 1

        all_combination = []

        if len(s) == 1 or len(set(s)) == 1:
            return [s]

        if len(filter(lambda x: x[1] % 2 == 1, Counter(s).items())) > 1:
            return []

        else:
            if len(s) % 2 == 0:
                if len(filter(lambda x: x[1] == 1, Counter(s).items())) == 1:
                    return []
                else:
                    result = []
                    word_frequency = Counter(s)
                    for letters in word_frequency:
                        result.extend(repeat(letters, word_frequency[letters] / 2))

                    for i in permutations("".join(result), len(result)):
                        all_combination.append("".join(list(i)) + "".join(list(i[::-1])))

                    return all_combination

            else:
                result = []
                word_frequency = Counter(s)
                for letters in word_frequency:
                    if word_frequency[letters] % 2 == 1:
                        middle_character = letters
                    result.extend(repeat(letters, word_frequency[letters] / 2))

                for i in permutations("".join(result), len(result)):
                    all_combination.append("".join(list(i)) + middle_character + "".join(list(i[::-1])))

                return all_combination

print Solution().generatePalindromes("aabaa")

