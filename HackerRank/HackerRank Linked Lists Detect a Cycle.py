"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head is None:
        return False

    tortoise = head
    hare = head

    while tortoise.next is not None and hare.next is not None:
        tortoise = tortoise.next
        
        if hare.next.next is not None:
            hare = hare.next.next
        else:
            return False

        if tortoise is hare:
            return True

    return False
