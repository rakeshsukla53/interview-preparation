
import math

class Solution(object):

    def isPrime(self, n):
        """
        Prime number test algorithm. It runs pretty blazing past
        """
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n**0.5)
        f = 5
        while f <= r:

            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f += 6

        return True

    # def factors(self, n):
    #
    #     for i in range(1, int(math.sqrt(n)) + 1):
    #         if n % i == 0:
    #             print [i, n // i]

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if 1 <= num < 7:
            return True

        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:

                if i not in {2: '', 3: '', 5: ''} and self.isPrime(i):
                    return False

                if num // i not in {2: '', 3: '', 5: ''} and self.isPrime(num // i):
                    return False

        return True

print Solution().isUgly(200000000)

