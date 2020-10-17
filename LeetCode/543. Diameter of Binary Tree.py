from typing import List

"""
Problem Name: 543. Diameter of Binary Tree

Problem URL: https://leetcode.com/problems/diameter-of-binary-tree/

Problem Section: Tree

Problem Statement:
 Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them. 

Resources:

runtime: 
106 / 106 test cases passed.
	Status: Accepted
Runtime: 48 ms
Memory Usage: 16.2 MB
"""

# Solution techniques are

# Time complexity : O() Space complexity : O()


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


myobj = Solution()
inpt = input
print(myobj.function_name(inpt))
