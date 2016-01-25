
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slow_pointer = head
        fast_pointer = slow_pointer

        while slow_pointer != None:
            if fast_pointer.next != None:
                fast_pointer = fast_pointer.next
                if fast_pointer.next != None:
                    fast_pointer = fast_pointer.next
                else:
                    return False
            else:
                return False
            if fast_pointer == slow_pointer:
                return True
            slow_pointer = slow_pointer.next

        return False


