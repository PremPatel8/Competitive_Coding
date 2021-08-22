from typing import List

"""
Problem Name: Sum of Two Integers

Problem URL: https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/

Problem Difficulty: Medium

Problem Section: Math, Bit Manipulation

Problem Statement:
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Resources:
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/discuss/84278/A-summary:-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/discuss/84282/Python-solution-with-no-%22+-*%22-completely-bit-manipulation-guaranteed

runtime: 
13 / 13 test cases passed.
	Status: Accepted
Runtime: 24 ms
Memory Usage: 14.1 MB
"""

# Solution techniques are Bit Manipulation

# Time complexity : O() Space complexity : O()


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


myobj = Solution()
a = -2
b = 3
# op = 1
print(myobj.getSum(a, b))
