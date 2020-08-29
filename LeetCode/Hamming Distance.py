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
Memory Usage: 13.7 MB """

# Solution techniques are Bit Manipulation
# Time complexity : O(1) Space complexity : O(1) Bit Manipulation trick using XOR and AND t&(t-1) trick
""" 
Each iteration of t & (t-1) removes the most right bit from your number. You increase the counter until your number becomes 0.
 """


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        xor_val = x ^ y

        while xor_val:
            res += 1
            xor_val = xor_val & (xor_val-1)

        return res


myobj = Solution()
x = 1
y = 4
print(myobj.hammingDistance(x, y))
