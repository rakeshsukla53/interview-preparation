
from collections import defaultdict

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            return item
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return None


def NumberOfPairs(a, k):

    a.sort()
    check_duplicate = defaultdict(int)
    count = 0
    for i in a:

        if binarySearch(a, k - i):
            if check_duplicate.has_key((i, k - i)):
                pass
            else:
                check_duplicate[(i, k - i)] += 1
                check_duplicate[(k - i, i)] += 1
                count += 1

    return count

print NumberOfPairs([6, 6, 3, 9, 3, 5, 1], 12)







