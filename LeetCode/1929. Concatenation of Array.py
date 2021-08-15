from typing import List

"""
Problem Name: 1929. Concatenation of Array

Problem URL: https://leetcode.com/problems/concatenation-of-array/

Problem Section: Array

Problem Difficulty: Easy

Problem Statement:
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]


Resources:

"""


class Solution:
    """
    Solution technique: Using + operator

    Time & Space Complexity:
    Time O(n)
    Space O(2n) ~ o(n)

    Runtime:
    91 / 91 test cases passed.
        Status: Accepted
    Runtime: 76 ms
    Memory Usage: 14.5 MB
    """

    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     nums = nums+nums
    #     return nums

    """
    Solution technique: Using extend()

    Time & Space Complexity:
    Time O(n)
    Space O(2n) ~ o(n)

    Runtime:
    91 / 91 test cases passed.
    Status: Accepted
    Runtime: 84 ms
    Memory Usage: 14.8 MB
    """

    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     nums.extend(nums)
    #     return nums

    """
    Solution technique: manually creating a list of size 2*n and assigning values to index i and i+n in a loop

    Time & Space Complexity:
    Time O(n)
    Space O(2n) ~ o(n)

    Runtime:
    91 / 91 test cases passed.
    Status: Accepted
    Runtime: 88 ms
    Memory Usage: 14.3 MB
    """

    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        res = [None] * (2*numsLen)

        for idx, no in enumerate(nums):
            res[idx] = no
            res[idx+numsLen] = no

        return res
