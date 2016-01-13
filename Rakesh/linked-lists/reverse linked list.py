
# Definition for singly-linked list.
# reversing linked list iteratively


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """ reverse the linked list iteratively
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        first = None
        while head != None:
            second = head.next
            head.next = first
            first = head
            head = second

        return first
