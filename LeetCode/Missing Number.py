from typing import List

"""
Problem Name: Missing Number

Problem Section: Others / Bit Manipulation

Problem Statement:
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Resources:

"""

""" runtime """

# Solution techniques are
# Time complexity : O(n**2) Space complexity : O(n) My solution using set intersection optimized


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        return (set(range(len(nums)+1)) - set(nums)).pop()


myobj = Solution()
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums = [3, 0, 1]
print(myobj.missingNumber(nums))
