__author__ = 'rakesh'

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        given a string, if you have to tell whether the string can be splitted into multiple words
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        #so here we will create a matrix of len(A) * len(A)

        dynamicMatrix = [[0 for item_idx in range(0, len(s))] for row_idx in range(0, len(s)) ]

        for i in range(1, len(s)+1):
            k = i
            for j in range(len(s) + 1 - i):
                word = s[j:k]
                #print word, j, k
                if len(word) == 1:
                    k += 1
                    continue
                for p in range(1, len(word)):
                    wordSplit1 = word[:p]
                    wordSplit2 = word[p:len(word)]
                    '''
                    here we just have to check with AND conditon whether it is present in the dictionary or not
                    '''

                k += 1

Solution().wordBreak('iamace', {})
