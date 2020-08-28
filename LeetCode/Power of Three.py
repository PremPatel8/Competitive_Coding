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
Runtime: 80 ms
Memory Usage: 13.8 MB """

# Solution techniques are
# Time complexity : O(log3n) Space complexity : O(1) Naive Iterative solution


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n / 3

        return True if n == 1 else False


myobj = Solution()
inpt = 45
print(myobj.isPowerOfThree(inpt))
