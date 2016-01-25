
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
    """
    def removeElements(self, head, val):
        self = ListNode(0)
        self.next, head = head, self
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return self.next


