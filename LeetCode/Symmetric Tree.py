from typing import List

"""
Problem Name: Symmetric Tree

Problem Section: Trees

Problem Statement:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3 

Follow up: Solve it both recursively and iteratively.

Resources:

"""
""" 195 / 195 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 13.8 MB """

# Solution techniques are Recursive and Iterative using queue (like BFS)
# Time complexity : O(n) Space complexity : O(n) Iterative solution using queue (like BFS)
""" Complexity Analysis
Time complexity : O(n) Because we traverse the entire input tree once, the total run time is O(n), where n is the total number of nodes in the tree.
Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n). 
Therefore, space complexity due to recursive calls on the stack is O(n)O(n)O(n) in the worst case.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque()

        queue.append(root.left)
        queue.append(root.right)

        while queue:
            t1 = queue.pop()
            t2 = queue.pop()

            if not t1 and not t2:
                continue
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False

            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

        return True


myobj = Solution()
node = None
print(myobj.isSymmetric(node))
