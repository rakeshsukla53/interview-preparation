__author__ = 'rakesh'

def findMax(value, M):
    '''
    find the continous subarray such that total sum module M is greatest
    :rtype : maximum value of subarray
    time complexity is O(n^2) here but we need to reduce it
    '''
    maxSubArraySum = 0
    for i in range(len(value)):
        sumValue = 0
        for j in range(i, len(value)):
            sumValue += value[j]
            if sumValue % M > maxSubArraySum:
                maxSubArraySum = sumValue % M
    return maxSubArraySum

testCases = raw_input()
for i in range(int(testCases)):
    moduloNumber = raw_input().strip().split(" ")[1]
    array = raw_input().strip().split(" ")
    array = map(int, array)
    print findMax(array, int(moduloNumber))

