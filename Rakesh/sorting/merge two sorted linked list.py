
# merge two sorted two linked list

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        merged_node = ListNode(0)
        head = merged_node

        while l1 and l2:
            
            if l2.val > l1.val:
                merged_node.next = ListNode(l1.val)
                merged_node = merged_node.next
                l1 = l1.next

            elif l1.val > l2.val:
                merged_node.next = ListNode(l2.val)
                merged_node = merged_node.next
                l2 = l2.next

            else:
                merged_node.next = ListNode(l2.val)
                merged_node = merged_node.next
                merged_node.next = ListNode(l1.val)
                merged_node = merged_node.next
                l1 = l1.next
                l2 = l2.next
                
        while l2:
            merged_node.next = ListNode(l2.val)
            merged_node = merged_node.next
            l2 = l2.next

        while l1:
            merged_node.next = ListNode(l1.val)
            merged_node = merged_node.next
            l1 = l1.next

        merged_node = head.next
        del head

        return merged_node

'''
very simple way to do it
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b


The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.

The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.

'''

