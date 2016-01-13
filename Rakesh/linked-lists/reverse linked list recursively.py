
class Solution(object):
    def reverseList(self, head, last=None):
        """ reverse the linked list recursively now
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return last

        second = head.next
        head.next = last
        last = head
        head = second
        return self.reverseList(head, last)

# if you can solve problems iteratively then you can solve using recursively as well

