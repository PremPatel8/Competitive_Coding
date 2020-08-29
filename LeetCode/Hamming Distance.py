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
Memory Usage: 13.8 MB """

# Solution techniques are Bit Manipulation
# Time complexity : O(1) Space complexity : O(1) Bit Manipulation using rigt shift


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        n = x ^ y

        while(n):
            count += n & 1
            n >>= 1

        return count


myobj = Solution()
x = 1
y = 4
print(myobj.hammingDistance(x, y))
