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
    node = DoublyLinkedListNode(data)

    # Insert node at the beginning of the list
    if cur.data > data or cur.data == data:
        node.next = cur
        cur.prev = node
        head = node
        return head

    # Insert node in the middle of the list
    while cur.next:
        if (cur.data < data and cur.next.data > data) or cur.data == data:
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node
            return head
        cur = cur.next

    # Insert node at the end of the list
    if cur.data < data or cur.data == data:
        node.prev = cur
        cur.next = node
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
