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
Runtime: 76 ms
Memory Usage: 14 MB """
# Solution techniques are

# Time complexity : O() Space complexity : O() alternate solution using simple search and replace to generate longest increasing subsequence array


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        sol = []
        for idx, num in enumerate(nums):
            if not sol:
                sol.append(num)
            elif num > sol[-1]:
                sol.append(num)
            else:
                for j in range(len(sol)):
                    if num <= sol[j]:
                        sol[j] = num
                        break

        return len(sol)


myobj = Solution()
inpt = [10, 9, 2, 5, 3, 7, 101, 18]
print(myobj.lengthOfLIS(inpt))
