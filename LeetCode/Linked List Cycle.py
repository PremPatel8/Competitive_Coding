from typing import List

"""
Problem Name: Linked List Cycle

Problem Section: Linked List

Problem Statement:
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?

Resources:

"""
""" 17 / 17 test cases passed.
	Status: Accepted
Runtime: 44 ms
Memory Usage: 17.1 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) two pointer with reversing the second half of the linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or head.next == None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or fast.next == None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


myobj = Solution()

print(myobj.hasCycle(node))
