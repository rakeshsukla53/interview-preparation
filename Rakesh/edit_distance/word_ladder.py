__author__ = 'rakesh'

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        editDistance = self.edit_distance(beginWord, endWord)
        if editDistance == 0:
            return 0

        wordList = list(wordList)
        count = 2
        for i in range(editDistance):
            for j in wordList:
                if self.edit_distance(beginWord, j) == 1:
                    count += 1
                    beginWord = j
                    wordList.remove(j)
                    if self.edit_distance(j, endWord) == 1:
                        return count
                    break

    def edit_distance(self, s1, s2):
        m = len(s1) + 1
        n = len(s2) + 1

        tbl = {}
        for i in range(m): tbl[i, 0] = i
        for j in range(n): tbl[0,j] = j
        for i in range(1, m):
            for j in range(1, n):
                cost = 0 if s1[i-1] == s2[j-1] else 1
                tbl[i, j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

        return tbl[i, j]


print Solution().ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log"])
# Convert this solution to use dictionary rather than list or set. So that you can have O(1) thing