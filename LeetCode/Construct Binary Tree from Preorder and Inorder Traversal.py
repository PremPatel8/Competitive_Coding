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
    # preIndex = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        for idx, node in enumerate(inorder):
            self.inorderIndex[node] = idx

        return self.buildBinaryTree(0, preorder, inorder, 0, len(inorder)-1)

    def buildBinaryTree(self, preIndex, preorder, inorder, start, end):
        if start > end or preIndex > len(preorder)-1:
            return None

        root = TreeNode(preorder[preIndex])
        # self.preIndex += 1

        if not root:
            return None

        if start == end:
            return root

        index = self.inorderIndex[root.val]

        root.left = self.buildBinaryTree(preIndex+1, preorder, inorder, start, index-1)
        root.right = self.buildBinaryTree(preIndex+index-start+1, preorder, inorder, index+1, end)

        return root
