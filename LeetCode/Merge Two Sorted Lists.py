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
Runtime: 34 ms
Memory Usage: 13.7 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) Alt Recursive solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a


myobj = Solution()

print(myobj.mergeTwoLists(node))
