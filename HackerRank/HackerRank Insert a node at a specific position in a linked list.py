#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtPosition(head, data, position):
    nodeToInsert = SinglyLinkedListNode(data)
    i = 0
    # insert a node to a empty linked list
    if head is None:
        return nodeToInsert
    # insert a node at the head of a linked list
    elif position == 0:
        nodeToInsert.next = head
        return nodeToInsert
    else:
        # insert a node in the middle or at the end of the linked list
        currPtr = head

        while(i < position-1 and currPtr.next is not None):
            currPtr = currPtr.next
            i += 1

        nodeToInsert.next = currPtr.next
        currPtr.next = nodeToInsert

        return head


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    # print_singly_linked_list(llist_head, ' ', fptr)
    # fptr.write('\n')

    # fptr.close()
