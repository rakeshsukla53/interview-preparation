
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import cPickle
from collections import defaultdict

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        store_objects = defaultdict(int)

        while head != None:
            if str(cPickle.dumps(head)) in store_objects:
                return True
            store_objects[str(cPickle.dumps(head))] += 1
            head = head.next

        return False

head = ListNode(10)
Solution().hasCycle(head)

# well this is not the right way to do that because it is highly inefficient method

# Floyd Marshall Algorithm is the right approach to go about it



