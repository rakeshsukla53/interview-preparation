

# program is giving correct result but start optimizing

class Solution(object):
    '''
    >>Solution().uniquePaths(10, 10)
    >> 48620
    '''

    def __init__(self):
        self.paths = 0

    def findpaths(self, m, n):

        if m == 1 and n == 1:
            self.paths += 1
        if m < 1 or n < 1:
            return

        self.findpaths(m - 1, n)
        self.findpaths(m, n - 1)

    def uniquePaths(self, m, n):

        self.findpaths(m, n)
        return self.paths

print Solution().uniquePaths(4, 4)

