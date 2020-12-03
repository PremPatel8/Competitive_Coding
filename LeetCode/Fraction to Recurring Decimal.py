from typing import List

"""
Problem Name: Fraction to Recurring Decimal

Problem URL: https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/821/

Problem Section: Math

Problem Statement:
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Constraints:
-231 <= numerator, denominator <= 231 - 1
denominator != 0

Resources:
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/821/discuss/51187/Python-easy-to-understand-solution

runtime: 
38 / 38 test cases passed.
	Status: Accepted
Runtime: 28 ms
Memory Usage: 14.5 MB
"""

# Solution techniques are Long Division

# Time complexity : O() Space complexity : O()


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        remainders = {}

        while remainder > 0 and remainder not in remainders:
            remainders[remainder] = len(result)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        if remainder in remainders:
            idx = remainders[remainder]
            result.insert(idx, '(')
            result.append(')')

        return ''.join(result).rstrip(".")


myobj = Solution()
numerator = 2
denominator = 1
print(myobj.fractionToDecimal(numerator, denominator))
