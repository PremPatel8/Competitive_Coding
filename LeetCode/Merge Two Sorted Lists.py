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
Memory Usage: 13.8 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) Optimized iterative solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2

        return dummy.next


myobj = Solution()

print(myobj.mergeTwoLists(node))
