from typing import List

"""
Problem Name: Validate Binary Search Tree

Problem Section: Trees

Problem Statement:
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Resources:

"""
""" 75 / 75 test cases passed.
	Status: Accepted
Runtime: 36/45 ms
Memory Usage: 16.3 MB """

# Solution techniques are Recursion, Iteration using Stack and DFS, Inorder traversal
# Time complexity : O(n) Space complexity : O(n) Recursive solution Time - since we visit each node exactly once, Space - since we keep up to the entire tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


myobj = Solution()

print(myobj.maxDepth(node))
