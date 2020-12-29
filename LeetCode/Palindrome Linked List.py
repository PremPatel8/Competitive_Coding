from typing import List

"""
Problem Name: Palindrome Linked List

Problem Section: Linked List

Problem Statement:
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

Resources:
https://www.youtube.com/watch?v=vHam6riSavo&feature=emb_logo
https://leetcode.com/problems/palindrome-linked-list/discuss/953534/Two-pointer-solution-wvideo-whiteboard-explanation

"""
""" 26 / 26 test cases passed.
	Status: Accepted
Runtime: 64 ms
Memory Usage: 24 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) two pointer with reversing the second half of the linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half
        prvnd = None
        while slow:
            nxtnd = slow.next
            slow.next = prvnd
            prvnd = slow
            slow = nxtnd

        # compare the first and second half nodes
        while prvnd:  # while node and head:
            if prvnd.val != head.val:
                return False
            prvnd = prvnd.next
            head = head.next
        return True


myobj = Solution()

print(myobj.mergeTwoLists(node))
