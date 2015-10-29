__author__ = 'rakesh'

"""
 Check if linked list has cycle
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return 0 if no cycle else return 1
"""
from collections import defaultdict

def HasCycle(head):

    if head is None:
        return 0

    count = 0
    while head.next != None:

        count += 1
        if count > 100:
            return 1

        head = head.next

    return 0








