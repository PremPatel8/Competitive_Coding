# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""91 / 91 test cases passed.
Runtime: 80 ms
Memory Usage: 17.7 MB"""


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k = k - 1

            if not k:
                return root.val

            root = root.right


tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.left.right = TreeNode(2)

myobj = Solution()

print(myobj.kthSmallest(tree, 1))
