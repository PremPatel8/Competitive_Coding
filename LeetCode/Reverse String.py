from typing import List

"""
Problem Name: Reverse String

Problem Section: String

Problem Statement:
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Resources:
"""
""" 1032 / 1032 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() string reverse solution cleaner code


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        res = sign * int(str(abs(x))[::-1])

        return res if res > -2**31 and res < 2**31-1 else 0


myobj = Solution()
inpt = 123
print(myobj.reverse(inpt))
