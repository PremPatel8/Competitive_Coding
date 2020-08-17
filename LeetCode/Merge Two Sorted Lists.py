from typing import List

"""
Problem Name: Merge Two Sorted Lists

Problem Section: Linked List

Problem Statement:
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Resources:

"""
""" 208 / 208 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() My solution using iteration and temp variable


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1 = l1
        c2 = l2
        head = None

        if not c1 or not c2:
            return c1 if not c2 else c2

        head = c1 if c1.val <= c2.val else c2

        while c1 and c2:
            if c1.val <= c2.val:
                while c1 and c2 and c1.val <= c2.val:
                    temp = c1
                    c1 = c1.next
                temp.next = c2

            elif c1.val > c2.val:
                while c1 and c2 and c1.val > c2.val:
                    temp = c2
                    c2 = c2.next
                temp.next = c1

        return head


myobj = Solution()

print(myobj.mergeTwoLists(node))
