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
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def BalancedBrackets(combination):
            stack = []

            for chr in combination:
                if chr == "(":
                    stack.append(chr)
                elif chr == ")":
                    if len(stack) == 0:
                        return False

                    top_element = stack.pop()

                    if not (top_element == "(" and chr == ")"):
                        return False

            if len(stack) != 0:
                return False

            return True

        def backtrack(combination, brackets):
            if brackets == 0:
                if BalancedBrackets(combination):
                    output.append(combination)
            else:
                for br in ["(", ")"]:
                    backtrack(combination+br, brackets-1)

        if n:
            backtrack("", 2*n)

        return output


myobj = Solution()

print(myobj.generateParenthesis(3))
