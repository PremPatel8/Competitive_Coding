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

""" 122 / 122 test cases passed.
	Status: Accepted
Runtime: 140 ms
Memory Usage: 15.1 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) Alt Gauss' solution


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = expected_sum = 0
        n = 1

        for no in nums:
            actual_sum += no
            expected_sum += n
            n += 1

        return expected_sum-actual_sum


myobj = Solution()
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums = [3, 0, 1]
print(myobj.missingNumber(nums))
