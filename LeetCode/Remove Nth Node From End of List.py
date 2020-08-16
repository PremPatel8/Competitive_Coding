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
Memory Usage: 13.8 MB """

# Solution techniques are
# Time complexity : O(1) Space complexity : O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        counter = 0
        curr = head

        node_addrs = []

        while curr != None:
            node_addrs.append(curr)
            curr = curr.next

        # print(f"node_addrs = {node_addrs}")

        node_before_index = len(node_addrs)-1-n

        # print(f"node_before_index = {node_before_index}")

        if node_before_index < 0:
            head = head.next
            return head
        else:
            node_before = node_addrs[node_before_index]

            # print(f"node_before = {node_before}")

            node_before.next = node_before.next.next

            return head


myobj = Solution()

print(myobj.removeNthFromEnd(node, 2))
