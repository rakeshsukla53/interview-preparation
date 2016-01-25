
from collections import defaultdict
from itertools import product
import sys

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.words = words
        self.dictionary = defaultdict(list)
        for index, word in enumerate(self.words):
            self.dictionary[word].append(index)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        shortest_distance = sys.maxint

        for index1, index2 in product(self.dictionary[word1], self.dictionary[word2]):

            if abs(index1 - index2) < shortest_distance:
                shortest_distance = abs(index1 - index2)

        return shortest_distance

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
