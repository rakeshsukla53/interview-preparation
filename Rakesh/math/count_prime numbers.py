
# Sieve of Eratosthenes

import math

class Solution(object):

    def isPrime(self, n):
        """
        Prime number test algorithm. It runs pretty fast
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

    def countPrimes(self, n):
        """
        Count the total number of prime numbers upto n based on sieve of eratosthenes algorithm
        :type n: int
        :rtype: int
        """
        total_prime = [True] * n
        total_prime[0], total_prime[1] = False, False

        # sieve of Eratosthenes algorithm
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if self.isPrime(i):
                total_prime[i] = True
                for j in xrange(i * i, n, i):  # another optimization for sieve of Eratosthenes
                    total_prime[j] = False

        return len(filter(lambda x: x, total_prime))

print Solution().countPrimes(499979)



Absolutely brilliant approach

class Solution:
# @param {integer} n
# @return {integer}
def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)

