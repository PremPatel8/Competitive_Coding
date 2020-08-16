from typing import List

"""
Problem Name: Remove Nth Node From End of List

Problem Section: Linked List

Problem Statement:
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?

Resources:

"""
""" 208 / 208 test cases passed.
	Status: Accepted
Runtime: 28 ms
Memory Usage: 13.9 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() two pointer technique


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


myobj = Solution()

print(myobj.removeNthFromEnd(node, 2))
