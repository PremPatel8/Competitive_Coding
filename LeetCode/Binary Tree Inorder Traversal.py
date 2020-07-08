from collections import deque

""" Given a binary tree, return the inorder traversal of its nodes' values. """

""" My Recursive Solution """


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def helper(node, output):
            if node:
                if node.left:
                    helper(node.left, output)

                output.append(node.val)

                if node.right:
                    helper(node.right, output)

        helper(root, output)

        return output


""" LeetCode Optimized Recursive Solution"""


def inorderTraversal(self, root: TreeNode) -> List[int]:
    def dfs(node, array):
        if not node:
            return
        dfs(node.left, array)
        array.append(node.val)
        dfs(node.right, array)

    res = []
    if not root:
        return res
    dfs(root, res)
    return res


""" LeetCode Stack based iterative solution """


def inorderTraversal(self, root: TreeNode) -> List[int]:
    output = []

    if not root:
        return output

    stack = deque()
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        output.append(curr.val)
        curr = curr.right

    return output
