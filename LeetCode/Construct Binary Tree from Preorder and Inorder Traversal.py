from collections import defaultdict
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    inorderIndex = defaultdict(int)
    preIndex = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        for idx, node in enumerate(inorder):
            self.inorderIndex[node] = idx

        return self.buildBinaryTree(preorder, inorder, 0, len(inorder)-1)

    def buildBinaryTree(self, preorder, inorder, start, end):
        if start > end or self.preIndex > len(preorder):
            return None

        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1

        if not root:
            return None

        if start == end:
            return root

        index = self.inorderIndex[root.val]

        root.left = self.buildBinaryTree(preorder, inorder, start, index-1)
        root.right = self.buildBinaryTree(preorder, inorder, index+1, end)

        return root
