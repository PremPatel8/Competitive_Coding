from typing import List

"""
Problem Name: 83. Remove Duplicates from Sorted List

Problem URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Problem Section: Linked List

Problem Statement:
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3

Resources:

runtime: 
165 / 165 test cases passed.
	Status: Accepted
Runtime: 40 ms
Memory Usage: 14 MB
"""

# Solution techniques are iterate through each node and check curr and curr.next vales, if same make curr point to next next node (skip the next node)

# Time complexity : O(n) Space complexity : O(1)
""" Complexity Analysis
Time complexity : O(n). Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is O(n), where n is the number of nodes in the list.
Space complexity : O(1). No additional space is used.
 """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
