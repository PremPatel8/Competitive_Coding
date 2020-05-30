"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


'''
Tortoise and Hare technique used, move the tortoise node one node at a time and
the hare node two nodes at a time. If there is a cycle in the Linked List they
will eventually meet, if not then either one of them will become Null and
we can stop checking any further
'''


def has_cycle(head):
    if head is None:
        return False

    fast = slow = head

    while fast.next is not None and slow.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            return True

    return False
