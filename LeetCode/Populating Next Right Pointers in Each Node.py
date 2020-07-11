from collections import deque

# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ans = root
        while root and root.left:
            curr = root

            while curr:
                curr.left.next = curr.right
                curr.right.next = curr.next.left if curr.next else None
                curr = curr.next

            root = root.left
        return ans