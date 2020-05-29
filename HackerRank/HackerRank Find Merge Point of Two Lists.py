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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def findMergeNode(head1, head2):
    cur1 = head1
    cur2 = head2
    diff = 0
    l1 = 0
    l2 = 0

    while(cur1 is not None):
        l1 += 1
        cur1 = cur1.next
    
    while(cur2 is not None):
        l2 += 1
        cur2 = cur2.next

    diff = l1-l2 if l1 > l2 else l2-l1

    if diff > 0:
        if l1 > l2:
            for _ in range(diff):
                head1 = head1.next
        else:
            for _ in range(diff):
                head2 = head2.next

    while head1 is not head2:
        head1 = head1.next
        head2 = head2.next

    if head1 is not None:
        return head1.data

    return None


if __name__ == '__main__':
    fptr = open('D:/GitHub/Cometitive_Coding/HackerRank/MergePoint_Opt.txt', 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next

        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()
