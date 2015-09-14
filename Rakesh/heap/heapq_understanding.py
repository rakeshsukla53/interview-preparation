__author__ = 'rakesh'

import heapq

data = [10, 100, 15, 1, 2, 3, 18, 23, 89]

heap = []
for i in data:

	heapq.heappush(heap, i)

heapq.heapify(heap) #default heapify is min heap

print heap  #sorted array if you don't have to worry about it

print heapq._heapify_max(heap)  #default heapify is min heap

print heap

#http://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php

#why we use heap and what are its advtanges than binary search trees
