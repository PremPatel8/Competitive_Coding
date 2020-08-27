from typing import List

"""
Problem Name: Maximum Subarray

Problem Section: Dynamic Programming

Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Resources:

"""
""" 202 / 202 test cases passed.
	Status: Accepted
Runtime: 60 ms
Memory Usage: 14.5 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) DP Kadane's Algorithm solution


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(curr_sum+nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


myobj = Solution()
inpt = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(myobj.maxSubArray(inpt))
