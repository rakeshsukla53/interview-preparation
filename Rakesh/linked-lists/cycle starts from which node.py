from collections import defaultdict

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# I used the hash function to uniquely identify the objects
class Solution(object):
    def detectCycle(self, head):
        """
        Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        store_object = defaultdict(int)

        while head.next != None:
            hash_value = hash(head)
            if hash_value in store_object:
                return head
            store_object[hash_value] += 1
            head = head.next

        return None

