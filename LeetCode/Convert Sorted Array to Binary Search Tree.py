from typing import List

"""
Problem Name: Convert Sorted Array to Binary Search Tree

Problem Section: Trees

Problem Statement:
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

Resources:

"""
""" 32 / 32 test cases passed.
	Status: Accepted
Runtime: 60 ms
Memory Usage: 16.1 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(N)O(n) in the case of skewed binary tree. Recusrive binary search solution


def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        prettyPrintTree(node.right, prefix +
                        ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix +
                        ("    " if isLeft else "│   "), True)

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        return self.helper(nums, 0, len(nums))

    def helper(self, nums, lower, upper):
        if lower == upper:
            return None

        mid = (lower + upper) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, lower, mid)
        node.right = self.helper(nums, mid+1, upper)

        return node


myobj = Solution()
inpt = [-10, -3, 0, 5, 9]
prettyPrintTree(myobj.sortedArrayToBST(inpt))
