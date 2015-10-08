__author__ = 'rakesh'

class Solution(object):
    def isValid(self, s):
        """
        I am going to use stack for this problem
        :type s: str
        :rtype: bool
        """
        brackets = list(s)
        result = []
        count = 0
        if len(brackets) <= 1:
            return False
        for i in brackets:
            if i in ['(', '{', '[']:
                result.append(i)
                count += 1
            elif i in [')', '}', ']']:
                if len(result) == 0:
                    return False
                checkBracket = result.pop()
                count -= 1
                if i == ')' and checkBracket == '(':
                    continue
                if i == '}' and checkBracket == '{':
                    continue
                if i == ']' and checkBracket == '[':
                    continue
                return False

        if count == 0:
            return True
        else:
            return False

print Solution().isValid("")

