from typing import List

"""
Problem Name: 226. Invert Binary Tree

Problem URL: https://leetcode.com/problems/invert-binary-tree/

Problem Section: Tree

Problem Statement:
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Resources:

runtime: 
68 / 68 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14.2 MB

"""

# Solution techniques are Recursive and Iterative

# Time complexity : O(n) Space complexity : O(n) / O(h) - N nodes, H height of Tree for Recursive
# Time complexity : O(n) Space complexity : O(n)- N nodes for Iterative


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive sol
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return None

    #     right = self.invertTree(root.right)
    #     left = self.invertTree(root.left)

    #     root.left = right
    #     root.right = left

    #     return root

    # Iterative sol
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = []
        queue.append(root)

        while queue:
            curr = queue.pop()
            curr.right, curr.left = curr.left, curr.right

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return root


myobj = Solution()
inpt = input
print(myobj.invertTree(inpt))
