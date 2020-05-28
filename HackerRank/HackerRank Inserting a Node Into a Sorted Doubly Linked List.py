#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


def sortedInsert(head, data):
    cur = head
    newNode = DoublyLinkedListNode(data)

    # Insert node into a empty list
    if head is None:
        return newNode

    # Insert node at the beginning of the list
    if cur.data >= data:
        newNode.next = cur
        cur.prev = newNode
        head = newNode
        return head

    # Insert node in the middle of the list or at the end
    while cur.next is not None and cur.next.data < newNode.data:
        cur = cur.next

    newNode.prev = cur
    newNode.next = cur.next
    cur.next = newNode

    # Check if new node is being inserted at the end of the linked list
    if cur.next is not None:
        cur.next.prev = newNode

    return head


if __name__ == '__main__':
    fptr = open(
        'D:/GitHub/Cometitive_Coding/HackerRank/NodeInsertion_DLL.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
