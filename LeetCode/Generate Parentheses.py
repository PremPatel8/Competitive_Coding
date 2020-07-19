from typing import List

"""
Problem Name: Generate Parentheses

Problem Section: Backtracking

Problem Statement: 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n=3
Output:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


myobj = Solution()

print(myobj.generateParenthesis(3))
