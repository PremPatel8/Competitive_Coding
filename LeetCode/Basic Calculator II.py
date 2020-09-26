from typing import List
# from collections import defaultdict

"""
Problem Name: Basic Calculator II

Problem Section: Array and Strings

Problem Statement:
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

Resources:
"""

""" 109 / 109 test cases passed.
	Status: Accepted
Runtime: 84 ms
Memory Usage: 15.6 MB """

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n)


class Solution:
    def calculate(self, s: str) -> int:
        inputstr = s.strip()

        if not inputstr:
            return 0

        num = 0
        stack = []
        sign = "+"

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))

                num = 0
                sign = s[i]

        return sum(stack)


myobj = Solution()
inpt = "3+2*2"
print(myobj.calculate(inpt))
