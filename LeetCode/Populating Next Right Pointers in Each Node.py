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
        if not root:
            return root

        temp = []
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node)

                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]

            i = 0
            while i < len(temp)-1:
                temp[i].next = temp[i+1]
                i += 1

            temp = []

        return root
