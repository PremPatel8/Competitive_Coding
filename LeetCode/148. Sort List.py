from typing import List

"""
Problem Name: 148. Sort List

Problem Section: Linked List

Problem Statement:
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Resources:
"""

""" 16 / 16 test cases passed.
	Status: Accepted
Runtime: 208 ms
Memory Usage: 23.3 MB """

# Solution techniques are Top Down Merge Sort, Bottom Up Merge Sort

# Time complexity : O(n log n) Space complexity : O(log n) Top Down Merge Sort


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        mid = self.getMid(head)

        l, r = self.sortList(head), self.sortList(mid)

        return self.merge(l, r)

    def getMid(self, head):
        fast, slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        start = slow.next
        slow.next = None
        return start

    def merge(self, l, r):
        if not l or not r:
            return l or r
        dummy = p = ListNode(0)
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next


myobj = Solution()
inpt = [4, 2, 1, 3]
print(myobj.sortList(inpt))
