
from itertools import combinations
from collections import defaultdict



def NumberOfPairs(a, k):

    check_duplicate = defaultdict(int)
    count = 0
    a.sort()
    for i in combinations(a, 2):

        x, y = i
        if x + y == k:
            if check_duplicate.has_key((x, y)):
                pass
            else:
                check_duplicate[(x, y)] += 1
                check_duplicate[(y, x)] += 1
                count += 1

    return count

print NumberOfPairs([6, 6, 3, 9, 3, 5, 1], 12)


