__author__ = 'rakesh'

#it is an linear time algorithm

import sys

def kadaneAlgorithm(array):
    '''
    :param array:
    :return: the maximum sum of the subarry and the indexes
    '''
    if len(array) < 1:
        return None
    maxCurr = -sys.maxint
    maxValue = -sys.maxint
    p, q, r, s = 0, 0, 0, 0
    for i in range(len(array)):
        if i == 0:
            maxCurr = array[i]
            maxValue = array[i]
        if i > 0:
            if array[i] + maxCurr > maxCurr or array[i] + maxCurr > 0:
                if array[i] > 0 and maxCurr <= 0:
                    p, q = i, i
                    maxCurr = array[i]
                    if maxCurr > maxValue:
                        maxValue = maxCurr
                        r, s = p, q
                elif array[i] > 0 and maxCurr >= 0:
                    q += 1
                    maxCurr = maxCurr + array[i]
                    if maxCurr > maxValue:
                        maxValue = maxCurr
                        r, s = p, q
                if array[i] < 0 and maxCurr + array[i] > 0:
                    q += 1
                    maxCurr = maxCurr + array[i]
                    if maxCurr > maxValue:
                        maxValue = maxCurr
                        r, s = p, q
            else:
                if array[i] > maxCurr:
                    maxCurr = array[i]
                    maxValue = maxCurr
                    p, q = i, i
                    r, s = p, q
                else:
                    maxCurr = array[i]
                    p, q = i, i

    return maxValue, r, s

print kadaneAlgorithm([-1, -1, 0, 4, -3, 5])

