__author__ = 'rakesh'

import itertools

min = 100000000

stringList = ['a', 'b', 'c', 'd', 'a']

matchedString = ""

for element in itertools.product([0, 4], [2], [3]):

    sortedList = sorted(list(element))

    differenceList = [t - s for s, t in zip(sortedList, sortedList[1:])]

    if min > sum(differenceList):

        min = sum(differenceList)
        sortedElement = sortedList

for i in range(sortedElement[0], sortedElement[len(sortedElement)-1]+1):

    matchedString += "".join(stringList[i]) + " "

