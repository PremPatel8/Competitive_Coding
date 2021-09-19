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
Runtime: 36 ms
Memory Usage: 19.9 MB
"""

# Solution techniques are
# Time complexity : O(n) Space complexity : O(n)(The extra space comes from implicit stack space due to recursion. The recursion could go up to nnn levels deep.) Recursive solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node, prev=None):
            # when we reach the None node, that means we have reached the end of the original linked list
            # and therefore the prev variable points to the new head of the reversed linked list which we return as the answer
            if not node:
                return prev

            n = node.next

            node.next = prev

            return reverse(n, node)

        return reverse(head)


myobj = Solution()

print(myobj.reverseList(node))
