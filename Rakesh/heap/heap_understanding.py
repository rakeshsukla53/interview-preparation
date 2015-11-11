
import heapq

data = [3, 2, 1, 5, 6, 4, 13, 24, 100, 1, 2, 3, 23]

# heapq._heapify_max(heap)  #if you want to sort the array based

heapq._heapify_max(data)

print data

print heapq.heappop(data)

heapq._heapify_max(data)

print heapq.heappop(data)

# converting the whole data structure into heap
# for _ in range(len(data)):
#     heapq.heappush(heap, _)









