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
""" 478 / 478 test cases passed.
	Status: Accepted
Runtime: 216 ms
Memory Usage: 18.2 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() My simple solution


class Solution:
    def reverseString(self, s: List[str]) -> None:
        arrlen = len(s)

        for i in range(arrlen//2):
            s[i], s[arrlen-i-1] = s[arrlen-i-1], s[i]


myobj = Solution()
inpt = ["h", "e", "l", "l", "o"]
print(myobj.reverseString(inpt))
