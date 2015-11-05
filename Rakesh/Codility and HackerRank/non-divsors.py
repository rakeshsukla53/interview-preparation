
import math
import bisect

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

def solution(A):
    # write your code in Python 2.7
    B = list(A)
    A.sort()  #nlogn
    result = []
    l = len(A)

    for i in B:
        j = bisect.bisect_right(A, i)  #logN
        divisors = list(divisorGenerator(i))
        while B[j - 1] == B[j - 2]:
            j -= 1
        k = len(set(A[:j]) - set(divisors))
        result.append(l - j + k)

    return result

print solution([3, 1, 2, 3, 6])


