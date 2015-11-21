
import math

def solution(N):
    # write your code in Python 2.7
    result = []

    if N == 1:
        return None

    # the range_value will always be less or equal to log(N,2) where N is the number, and 2 is base
    # 2^x = N => x = log2N
    # math.ceil function return the ceiling of x as a float, the smallest integer value greater than or equal to x.
    range_value = int(math.ceil(math.log(N, 2)))

    for i in range(range_value):

        if N % pow(2, i) == 0:
            result.append(i)

    return result[-1]

