from typing import List
from collections import deque

"""
Problem Name: Letter Combinations of a Phone Number

Problem Section: Backtracking

Probelm Statement: 
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

1:None, 2:a,b,c, 3:d,e,f
4:g,h,i, 5:j,k,l, 6:m,n,o
7:p,q,r,s, 8:t,u,v, 9:w,x,y,z

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

# LeetCode official solution, backtracking based approach
"""
25 / 25 test cases passed.
Status: Accepted
Runtime: 32 ms
Memory Usage: 13.8 MB
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


myobj = Solution()

print(myobj.letterCombinations("23"))