from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res, temp = [], []
        flag = True
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]

            if not flag:
                temp.reverse()

            res += [temp]

            temp = []
            flag = not flag

        return res


root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(8)
root.left.right = TreeNode(12)
root.right.left = TreeNode(16)
root.right.right = TreeNode(25)

myobj = Solution()

print(myobj.zigzagLevelOrder(root))

# ans [[15], [20, 10], [8, 12, 16, 25]]
