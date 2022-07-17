# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Your code took 5 milliseconds — faster than 78.17% in Python
    def solve(self, root):
        res = [0, 0]

        def dfs(node):
            if node:
                if not node.left and not node.right:
                    res[0] += 1
                else:
                    res[1] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return res
