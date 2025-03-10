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
Memory Usage: 13.8 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() optimized mathematical div & mod solution


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

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        arrLen = len(s)

        for idx in range((arrLen//2)):
                temp = s[idx]
                s[idx] = s[arrLen-idx-1]
                s[arrLen-idx-1] = temp

        print(f"Reversed String = {s}")


myobj = Solution()
inpt = 1534236469
print(myobj.reverse(inpt))
