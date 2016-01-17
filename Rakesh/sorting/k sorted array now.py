
import heapq

def k_sorted_array(lists):

    result = []

    heapq.heapify(lists)
    while lists:  # this will take k
        pop = heapq.heappop(lists)

        if pop:
            result.append(pop.pop(0))
            heapq.heappush(lists, pop)  # this will take log(n) depending on the size of n

    return result

print k_sorted_array([[1, 2, 3], [3, 4, 5], [7, 8, 9], [0, 1, 2], [1, 2, 100]])

# overall complexity is k * log(n)

# merge two sorted list can also be done in this way!

