# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" 91 / 91 test cases passed.
Runtime: 104 ms
Memory Usage: 18 MB """

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        counter = 0
        leafReached = False
        ans = 0

        def helper(node):
            if not node:
                nonlocal leafReached
                leafReached = True
                return

            helper(node.left)

            if leafReached:
                nonlocal counter
                counter += 1

            if counter == k:
                nonlocal ans
                ans = node.val

            helper(node.right)

            return ans

        return helper(root)


tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.left.right = TreeNode(2)

myobj = Solution()

print(myobj.kthSmallest(tree, 1))
