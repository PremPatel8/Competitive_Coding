from typing import List

"""
Problem Name: Excel Sheet Column Number

Problem Section: Math

Problem Statement:
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701

Constraints:
1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".

Resources:

"""

""" 1000 / 1000 test cases passed.
	Status: Accepted
Runtime: 28 ms
Memory Usage: 13.9 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) Base 26 solution


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0

        for i in s:
            res = res*26 + ord(i)-ord('A')+1

        return res


myobj = Solution()
inpt = "FXSHRXW"
print(myobj.titleToNumber(inpt))
