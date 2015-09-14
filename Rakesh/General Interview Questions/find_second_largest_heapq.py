__author__ = 'rakesh'

import heapq


#using heapify we can convert this whole

A = [10, 20, 30, 40, 50, 60, 70, 30, 20, 11, 15, 16, 19, 23]

heapq._heapify_max(A)
print heapq.heappop(A)
heapq._heapify_max(A)
print heapq.heappop(A)

#this is another method of find second largest element