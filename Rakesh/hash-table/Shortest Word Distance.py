
from collections import defaultdict
from itertools import product
import sys

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dictionary = defaultdict(list)
        for index, word in enumerate(words):
            dictionary[word].append(index)

        shortest_distance = sys.maxint

        for index1, index2 in product(dictionary['practice'], dictionary['coding']):

            if abs(index1 - index2) < shortest_distance:
                shortest_distance = abs(index1 - index2)
                # the distance cannot be shorter then one
                if shortest_distance == 1:
                    break

        return shortest_distance


print Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes", "practice", "coding"], 'practice', 'coding')


