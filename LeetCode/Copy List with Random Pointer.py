from typing import List

"""
Problem Name: Copy List with Random Pointer

Problem Section: Linked List

Problem Statement:
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

Example1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Constraints:
-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
The number of nodes will not exceed 1000.


Resources:
"""

""" 19 / 19 test cases passed.
	Status: Accepted
Runtime: 40 ms
Memory Usage: 14.6 MB """

# Solution techniques are

# Time complexity : O() Space complexity : O()


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        iter = head

        while iter:
            currDup = Node(iter.val, iter.next)
            currDup.next = iter.next
            iter.next = currDup
            iter = currDup.next

        iter = head

        while iter:
            if iter.random:
                iter.next.random = iter.random.next

            iter = iter.next.next

        iter = head
        copy = head_copy = head and head.next

        while iter:
            iter.next = iter = copy.next
            copy.next = copy = iter and iter.next

        return head_copy


myobj = Solution()
inpt = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
print(myobj.copyRandomList(inpt))
