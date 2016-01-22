
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_1 = len(s)
        len_2 = len(t)

        if abs(len_1 - len_2) > 1 or (len(list(set(s) - set(t))) > 1 or len(list(set(t) - set(s))) > 1) or (not s and not t):
            return False

        if abs(len_1 - len_2) == 1 or (len(list(set(s) - set(t))) > 1 or len(list(set(t) - set(s))) > 1):
            return False

        if abs(len_1 - len_2) == 0 or (len(list(set(s) - set(t))) > 1 or len(list(set(t) - set(s))) > 1):
            return False

        x = [[0]*(len_2+1) for _ in range(len_1+1)]   # the matrix whose last element -> edit distance
        for i in range(0, len_1+1):  # initialization of base case values
            x[i][0] = i
        for j in range(0, len_2+1):
            x[0][j] = j
        for i in range(1, len_1+1):
            for j in range(1, len_2+1):
                if s[i-1] == t[j-1]:
                    x[i][j] = x[i-1][j-1]
                    if x[i][j] > 1:  # for one edit distance problem this value should remain one till the end
                        return False
                else:
                    x[i][j] = min(x[i][j-1], x[i-1][j], x[i-1][j-1]) + 1

        return True

print Solution().isOneEditDistance('abbd', 'abd')






