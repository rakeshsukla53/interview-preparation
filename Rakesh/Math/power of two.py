

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and pow(2, 60) % n == 0

print Solution().isPowerOfTwo(8)

# Another very powerful solution

def isPowerOfTwo(self, n):
    return (n>0) and (n & (n-1))==0

