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
Runtime: 28 ms
Memory Usage: 14 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() My simple solution using string reverse


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(x)[1:]
            s = s[::-1]
            s = "-"+s
        else:
            s = str(x)
            s = s[::-1]

        res = int(str(s))

        return res if res > -2**31 and res < 2**31-1 else 0


myobj = Solution()
inpt = 123
print(myobj.reverse(inpt))
