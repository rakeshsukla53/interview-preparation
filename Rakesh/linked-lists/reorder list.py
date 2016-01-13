
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        end_pointer = head
        # go to the end of the linked list
        while end_pointer != None:
            end_pointer = end_pointer.next

        while end_pointer != head:
            end_pointer.next = head.next
            head.next = end_pointer
