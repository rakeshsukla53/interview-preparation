from itertools import islice
import heapq

def nlargest(n, iterable):
    """Find the n largest elements in a dataset.

    Equivalent to:  sorted(iterable, reverse=True)[:n]
    """
    if n < 0:
        return []
    it = iter(iterable)
    result = list(islice(it, n))
    if not result:
        return result
    heapq.heapify(result)
    _heappushpop = heapq.heappushpop
    for elem in it:
        _heappushpop(result, elem)
    result.sort(reverse=True)
    return result

print nlargest(5, [10, 122, 2, 3, 3, 4, 5, 5, 10, 12, 23, 18, 17, 15, 100, 101])

# Crucially Insert is O(log n) which beats O(n) for a sorted list.
