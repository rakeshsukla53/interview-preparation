class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = filter(None, s.split(' '))
        if len(s) == 0:
            return ""
        reverse_string = []
        for i in range(len(s) - 1, -1, -1):
            reverse_string.append(s[i])
        return " ".join(reverse_string)

print Solution().reverseWords("the sky is blue")
