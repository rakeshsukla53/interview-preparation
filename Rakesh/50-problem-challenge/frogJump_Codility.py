__author__ = 'rakesh'

from collections import defaultdict

def solution(A, X, D):
    '''
    find the earliest time to reach the other end
    :param A: Position and time values
    :param X: total length of the position
    :param D: Maximum jump distance
    :return: earliest time to reach the other end
    '''

    positionTime = defaultdict(int)  #Dictionary of position time
    earliestTime = []
    if D > X:
        return 0

    if min(A) > D:
        return -1

    for i in range(len(A)):  #put all the values here
        if not positionTime.has_key(A[i]):
            positionTime[A[i]] = i

    position = X - D

    while True:
        if 0 >= position:
            break
        if positionTime.has_key(position):
            earliestTime.append(positionTime[position])
            position = position - D
            X = X - D
        else:
            position += 1
            if position == X:
                return -1

    return max(earliestTime)


#print solution([1,9], 11, 2)


