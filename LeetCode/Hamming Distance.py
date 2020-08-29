from typing import List

"""
Problem Name: Hamming Distance

Problem Section: Others / Bit Manipulation

Problem Statement:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

Resources:
https://www.programiz.com/python-programming/operators
"""
""" 149 / 149 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 13.9 MB """

# Solution techniques are Bit Manipulation
# Time complexity : O(1) Space complexity : O(1) Bit Manipulation trick using XOR and count


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


myobj = Solution()
x = 1
y = 4
print(myobj.hammingDistance(x, y))
