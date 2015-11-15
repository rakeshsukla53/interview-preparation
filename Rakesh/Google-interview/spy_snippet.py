
import itertools

import sys

def answer(document, searchTerms):

    min = sys.maxint

    matchedString = ""

    stringList = document.split(" ")

    d = dict()

    for j in range(len(searchTerms)):

        for i in range(len(stringList)):

            if searchTerms[j] == stringList[i]:

                d.setdefault(searchTerms[j], []).append(i)

    for element in itertools.product(*d.values()):

        sortedList = sorted(list(element))

        differenceList = [t - s for s, t in zip(sortedList, sortedList[1:])]

        if min > sum(differenceList):

            min = sum(differenceList)
            sortedElement = sortedList

            if sum(differenceList) == len(sortedElement) - 1:
                break

    try:
        for i in range(sortedElement[0], sortedElement[len(sortedElement)-1]+1):

            matchedString += "".join(stringList[i]) + " "

    except:
        pass

    return matchedString

print answer('''b d a c a c c d a''', ["a", "c", "d"])

