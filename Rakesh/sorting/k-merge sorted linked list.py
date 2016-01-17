# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """  this concept is used exactly in external sorting as well
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        minHeap = [(l.val, l) for l in lists if l]
        heapq.heapify(minHeap)

        dummy = head = ListNode(0)

        while minHeap:
            pop = heapq.heappop(minHeap)[1]
            if pop:
                dummy.next = pop
                dummy = dummy.next
                curr = pop.next
                if curr:
                    heapq.heappush(minHeap, (curr.val, curr))

        return head.next

