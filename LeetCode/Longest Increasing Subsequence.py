from typing import List

"""
Problem Name: Longest Increasing Subsequence

Problem Section: Dynamic Programming

Problem Statement:
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Resources:
https://leetcode.com/articles/longest-increasing-subsequence/#
"""

""" 24 / 24 test cases passed.
	Status: Accepted
Runtime: 48 ms
Memory Usage: 14 MB """
# Solution techniques are Dynamic Programming, Patience Sort using Binary Search

# Time complexity : O(n log n) Space complexity : O(n) alternate solution using Patience Sort which uses Binary Search


class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


myobj = Solution()
inpt = [10, 9, 2, 5, 3, 7, 101, 18]
print(myobj.lengthOfLIS(inpt))
