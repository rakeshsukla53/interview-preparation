# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """ merging k lists using heap also same as external sorting functionality
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        A = [(l.val, l) for l in lists]
        heapq.heapify(A)
