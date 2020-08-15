from typing import List
import string
"""
Problem Name: String to Integer (atoi)

Problem Section: String

Problem Statement:
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:
    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42

Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Resources:
"""
""" 1079 / 1079 test cases passed.
	Status: Accepted
Runtime: 40 ms
Memory Usage: 13.9 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O()


class Solution:
    def myAtoi(self, str: str) -> int:
        ls = list(str.strip())

        if len(ls) == 0:
            return 0

        sign = -1 if ls[0] == '-' else 1

        if ls[0] in ['-', '+']:
            del ls[0]

        ret, i = 0, 0

        while i < len(ls) and ls[i].isdigit():
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1

        return max(-2**31, min(sign * ret, 2**31-1))


myobj = Solution()
# inpt = "42"
# inpt = "   -42"
# inpt = "4193 with words"
# inpt = "words and 987"
# inpt = "-91283472332"
# inpt = "3.14159"
# inpt = "    "
# inpt = "+"
# inpt = "-+2"
print(myobj.myAtoi(inpt))
