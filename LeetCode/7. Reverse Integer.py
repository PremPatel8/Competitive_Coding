from typing import List

"""
Problem Name: 7. Reverse Integer

Problem URL: https://leetcode.com/problems/reverse-integer/

Problem Section: 

Problem Statement:
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Resources:

runtime: 
1032 / 1032 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14.1 MB

Complexity Analysis
Time Complexity: O(log⁡(x)). There are roughly log⁡10(x) digits in x.
Space Complexity: O(1).
"""

# Solution techniques are

# Time complexity : O() Space complexity : O()


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            pop = x % 10
            newRes = res*10 + pop

            if newRes > (2**31-1) or newRes < (-2**31):
                return 0

            res = newRes
            x = x // 10

        return sign*res


myobj = Solution()
# inpt = 123  # output = 321
inpt = -123  # output = -321
# inpt = 120  # output = 21
# inpt = 0  # output = 0
print(myobj.reverse(inpt))
