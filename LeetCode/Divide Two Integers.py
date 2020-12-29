from typing import List

"""
Problem Name: Divide Two Integers

Problem URL: https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/820/

Problem Section: Math

Problem Statement:
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0


Resources:

runtime: 
989 / 989 test cases passed.
	Status: Accepted
Runtime: 20 ms
Memory Usage: 14.3 MB
"""

# Solution techniques are bit manipulation

# Time complexity : O() Space complexity : O()


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            x = 0
            while dividend >= divisor << (x + 1):
                x += 1
            res += 1 << x
            dividend -= divisor << x
        return min(res if sig else -res, 2147483647)


myobj = Solution()
dividend = 10
divisor = 3
print(myobj.divide(dividend, divisor))
