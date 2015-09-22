__author__ = 'rakesh'


def findMax(value, M):
    '''
    find the continous subarray such that total sum module M is greatest
    :rtype : maximum value of subarray
    time complexity is O(n^2) here but we need to reduce it
    '''


testCases = raw_input()
for i in range(int(testCases)):
    moduloNumber = raw_input().strip().split(" ")[1]
    array = raw_input().strip().split(" ")
    array = map(int, array)
    print findMax(array, int(moduloNumber))