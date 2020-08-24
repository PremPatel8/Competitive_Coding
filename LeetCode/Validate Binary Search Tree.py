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
Runtime: 48 ms
Memory Usage: 16 MB """

# Solution techniques are Recursion, Iteration using Stack and DFS, Inorder traversal
# Time complexity : O(n) Space complexity : O(n) Inorder traversal solution
# Time complexity : O(N)in the worst case when the tree is BST or the "bad" element is a rightmost leaf.
# Space complexity : O(N) to keep stack.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


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


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    stack = []
    inorder = float('-inf')

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        # If next element in inorder traversal
        # is smaller than the previous one
        # that's not BST.
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right

    return True


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            node = stringToTreeNode(line)

            print(isValidBST(node))

            prettyPrintTree(node)
        except StopIteration:
            break


if __name__ == '__main__':
    main()


# Input = [5, 1, 4, null, null, 3, 6], False
# [2,1,3], True
