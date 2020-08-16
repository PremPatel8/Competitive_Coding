from typing import List

"""
Problem Name: Reverse Linked List

Problem Section: Linked List

Problem Statement:
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?

Resources:

"""
""" 27 / 27 test cases passed.
	Status: Accepted
Runtime: 26 ms
Memory Usage: 15.2 MB
"""

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) My solution using iteration and temp and prev pointer


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


myobj = Solution()

print(myobj.reverseList(node))
