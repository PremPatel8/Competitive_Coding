from typing import List

"""
Problem Name: 876. Middle of the Linked List

Problem URL: https://leetcode.com/problems/middle-of-the-linked-list/

Problem Section: Linked List

Problem Statement:
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Examples:
Input: [1,2,3,4,5]
Output: Node 3

Input: [1,2,3,4,5,6]
Output: Node 4

Note:
The number of nodes in the given list will be between 1 and 100.


Resources:

runtime: 
15 / 15 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14.3 MB
"""

# Solution techniques Slow and Fast pointer, add each node to linked list, return A[A.length // 2]

# Time complexity : O(n) Space complexity : O(1) Slow and fast pointer technique


""" 
Time - O(n), Space - O(n)
class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2] """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
