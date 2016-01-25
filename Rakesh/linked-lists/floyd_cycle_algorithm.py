
def HasCycle(head):

    if head is None:
        return 0

    slow_pointer = head
    fast_pointer = slow_pointer

    while slow_pointer.next != None:

        fast_pointer = slow_pointer.next.next

        if fast_pointer == slow_pointer:
            return 1
        slow_pointer = slow_pointer.next
    return 0

