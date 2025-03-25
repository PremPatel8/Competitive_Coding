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
        def reverse(curr_node, prev=None):
            # when we reach the None node, that means we have reached the end of the original linked list
            # and therefore the prev variable points to the new head of the reversed linked list which we return as the answer
            if not curr_node:
                return prev

            next_node = curr_node.next

            curr_node.next = prev

            return reverse(next_node, curr_node) # recursive call where we pass the next node as the current node and the current node as the previous node

        return reverse(head)

    # Iterative Solution
    # Time complexity : O(n) Space complexity : O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev


myobj = Solution()

print(myobj.reverseList(node))
