from collections import defaultdict

class Solution(object):

    def __init__(self):
        self.graph = defaultdict(list)
        self.result = []

    def find_all_sentences(self, start, end, path=[]):
        path = path + [start]
        if path[-1] == end:
            return path
        for value in self.graph[start]:
            newPath = self.find_all_sentences(value, end, path)
            if newPath:
                self.result.append(newPath)


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # proving whether break is possible or not
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True

        path = []
        # capturing each break points in the sentence based on the dictionary provided
        for index, value in enumerate(d):
            if value:
                path.append(index)

        start, end = [], path[-1]

        i = 0
        # find the values of start point
        while path[i] + 1 == path[i + 1]:
            start.extend([path[i], path[i + 1]])
            i += 1

        # create graph for backtracking
        for i in range(len(path) - 1):
            j = i
            while path[j] + 1 == path[j + 1]:
                j += 1
            self.graph[path[i]] = path[j+1:]

        # find all the backtracking points
        for start_point in start:
            self.find_all_sentences(start_point, end)

        print self.result

s = "catsanddog"

dict = {"cat": '', "cats": '', "and": '',  "sand": '',  "dog": ''}
Solution().wordBreak(s, dict)
