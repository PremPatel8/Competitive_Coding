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
https://leetcode.com/problems/reverse-integer/discuss/4527/A-Python-solution-O(n)-58ms
https://leetcode.com/problems/reverse-integer/discuss/132861/3-lines-Python-Solution

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
    """ def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            res = res * 10 + x % 10
            x //= 10

        return 0 if res > pow(2, 31) else sign*res """

    # String reverse sol
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        rev_str_x = str(x)[::-1]
        res = int(rev_str_x)

        return 0 if res > pow(2, 31) else res * sign
        # return res*sign if -(2**31)-1 < res < 2**31 else 0


# myobj = Solution()
# inpt = 123  # output = 321
# inpt = -123  # output = -321
# inpt = 120  # output = 21
# inpt = 0  # output = 0
# print(myobj.reverse(inpt))

def test_reverse_positive_integer():
    assert Solution().reverse(123) == 321


def test_reverse_negative_integer():
    assert Solution().reverse(-123) == -321


def test_reverse_integer_zero_end():
    assert Solution().reverse(120) == 21


def test_reverse_0():
    assert Solution().reverse(0) == 0
