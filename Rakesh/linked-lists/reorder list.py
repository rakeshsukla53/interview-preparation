
class Solution(object):

    def reverseList(self, head, last=None):
        """ reverse the linked list recursively
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

    def reorderList(self, head):
        """ reorder the list
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        # count total number of nodes
        count = 0
        start_head = head
        while head.next != None:
            count += 1
            head = head.next
        head = start_head

        split_point = count / 2

        while split_point <= 0:
            head = head.next
            split_point -= 1

        last_point = self.reverseList(head)
        head = start_head
        while start_head != last_point:
            last_first = last_point.next
            last_point.next = head.next
            start_head.next = last_point

            start_head = last_point.next
            last_point = last_first

        return head
