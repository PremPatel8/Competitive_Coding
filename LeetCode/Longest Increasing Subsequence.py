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
Runtime: 1052 ms
Memory Usage: 14 MB """
# Solution techniques are

# Time complexity : O(n*2) Space complexity : O(n) Dynamic Programming solution


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        dp = [0]*len(nums)
        dp[0] = 1
        maxans = 1

        for i in range(1, len(nums)):
            maxvalUptpoI = 0

            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxvalUptpoI = max(maxvalUptpoI, dp[j])

            dp[i] = maxvalUptpoI+1
            maxans = max(maxans, dp[i])

        return maxans


myobj = Solution()
inpt = [10, 9, 2, 5, 3, 7, 101, 18]
print(myobj.lengthOfLIS(inpt))
