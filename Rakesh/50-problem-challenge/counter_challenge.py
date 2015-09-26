__author__ = 'rakesh'

def solution(N, A):
    '''
    :param N: Maximum value
    :param A: List of Numbers
    :return: List of numbers
    '''
    maxValue = 0
    counters = [0] * N
    for i in A:
        if (i >= 1) and (i <= N):
            counters[i - 1] += 1
            maxValue = counters[i - 1]
        elif i == N + 1:
            for k in range(len(counters)):
                counters[k] = maxValue
        else:
            pass

    return counters

print solution(5, [3, 4, 4, 6, 1, 4, 4])
