from typing import List
"""
Problem Name: Plus One

Problem Section: Array

Problem Statement:
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Resources:
"""
""" 109 / 109 test cases passed.
	Status: Accepted
Runtime: 28 ms
Memory Usage: 13.8 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) further optimized solution


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for idx in range(n-1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits


myobj = Solution()
# inpt = [1, 2, 3]
# inpt = [4, 3, 2, 1]
inpt = [9,9,9,9,9]
print(myobj.plusOne(inpt))
