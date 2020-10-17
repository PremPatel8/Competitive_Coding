from typing import List

"""
Problem Name: 617. Merge Two Binary Trees

Problem URL: https://leetcode.com/problems/merge-two-binary-trees/

Problem Section: Tree

Problem Statement:
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

 

Note: The merging process must start from the root nodes of both trees.


Resources:

runtime: 
Recursive:
183 / 183 test cases passed.
	Status: Accepted
Runtime: 88 ms
Memory Usage: 15.1 MB

"""

# Solution techniques are

# Time complexity : O(m) Space complexity : O(m), In average case, depth will be O(log m)
#  m represents the minimum number of nodes from the two given trees.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


myobj = Solution()
inpt = input
print(myobj.mergeTrees(inpt))
