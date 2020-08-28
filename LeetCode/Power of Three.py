from typing import List

"""
Problem Name: Power of Three

Problem Section: Math

Problem Statement:
Given an integer, write a function to determine if it is a power of three.

Example:
Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 4:
Input: 45
Output: false


Resources:

"""
""" 21038 / 21038 test cases passed.
	Status: Accepted
Runtime: 76 ms
Memory Usage: 13.8 MB """

# Solution techniques are
# Time complexity : O(1) Space complexity : O(1) Optimized Integer Limitations solution


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 == 3**19 % n


myobj = Solution()
inpt = 45
print(myobj.isPowerOfThree(inpt))
