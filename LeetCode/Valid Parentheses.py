from typing import List
from collections import deque

"""
Problem Name: Valid Parentheses

Problem Section: Others / Bit Manipulation

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example:
Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Resources:

"""

""" 91 / 91 test cases passed.
	Status: Accepted
Runtime: 24 ms
Memory Usage: 14 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(n) My solution using Queue


class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = deque()
        pairs_dict = {'(': ')', '[': ']', '{': '}'}

        for para in s:
            if para in pairs_dict:
                p_stack.append(para)
            else:
                if p_stack:
                    left_p = p_stack.pop()

                    if pairs_dict[left_p] != para:
                        return False
                else:
                    return False

        return True if len(p_stack) == 0 else False


myobj = Solution()
# s = "()[]{}"
# s = "([)]"
# s = "{[]}"
s = '['
print(myobj.isValid(s))
