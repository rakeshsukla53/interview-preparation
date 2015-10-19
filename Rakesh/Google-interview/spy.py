__author__ = 'rakesh'

import itertools, math

import sys

def answer(document, item_position):

    min_score = sys.maxint

    stringList = document.split(" ")

    d = dict()

    for j in range(len(item_position)):

        for i in range(len(stringList)):

            if item_position[j] == stringList[i]:

                d.setdefault(item_position[j], []).append(i+1)

    matchedString = None

    for term in d.keys():  # ignore duplicate terms
        for searchTerm in d[term]:
            item_position = [searchTerm]
            for other_term in d.keys():
                distances = [int(math.fabs(searchTerm - x)) for x in d[other_term]]
                item_position.append(d[other_term][distances.index(min(distances))])
            score = max(item_position) - min(item_position) + 1
            if score < min_score:
                matchedString = (min(item_position) - 1, max(item_position),)
                min_score = score

    return " ".join(stringList[slice(*matchedString)])


