from typing import List

"""
Problem Name: Maximum Depth of Binary Tree

Problem Section: Trees

Problem Statement:
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.

Resources:

"""
""" 39 / 39 test cases passed.
	Status: Accepted
Runtime: 36 ms
Memory Usage: 15 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(n) Iterative BFS solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)

            while size > 0:
                front = queue.popleft()

                if front.left:
                    queue.append(front.left)

                if front.right:
                    queue.append(front.right)

                size -= 1

            depth += 1

        return depth


myobj = Solution()

print(myobj.maxDepth(node))



""" 
39 / 39 test cases passed.
	Status: Accepted
Runtime: 40 ms
Memory Usage: 14.9 MB

def maxDepth(self, root):
    depth = 0
    level = [root] if root else []
    while level:
        depth += 1
        queue = []
        for el in level:
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
        level = queue
        
    return depth
 """