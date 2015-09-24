__author__ = 'rakesh'

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is not None:
            finalResult = 0
            for i in range(len(s)):
                frequency = {}
                count = 0
                for j in range(i, len(s)):
                    if not frequency.has_key(s[j]):
                        frequency[s[j]] = ''
                        count += 1
                    else:
                        if count > finalResult:
                            finalResult = count
                        count = 0
                    if count > finalResult:
                        finalResult = count

            return finalResult

value = Solution()
print value.lengthOfLongestSubstring('pwwkew')

