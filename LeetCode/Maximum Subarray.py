from typing import List

"""
Problem Name: Maximum Subarray

Problem URL: https://leetcode.com/problems/maximum-subarray/

Problem Difficulty: Easy

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
Runtime: 68 ms
Memory Usage: 14.6 MB """

# Solution techniques are Dynamic Programming and Kadane's Algo:

# the max subarray sum at index i is either the max_sum for subarray ending at [i-1] + nums[i] or nums[i]
# (either we extend the prev subarry by adding nums[i] or start a new subarray from index i)
# find the max_price till index i, by using DP to keep track of max_price at each index i-1
# We can use a DP array (Linear Space) to store the max_price of subarray till each index i
# Then we can use the following formula to calculate min price at i:
# local_maximum[i] = max(A[i]+local_maximum[i-1], A[i])
# We can also convert it to (constant space) DP by storing the last curr sum in the curr_sum variable, as we only need the sum value till the last index
# update max_sum if it's less than curr_sum at price i

# Time complexity : O(n) Space complexity : O(1) DP Kadane's Algorithm Pythonic solution


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(curr_sum+num, num)
            max_sum = max(max_sum, curr_sum)

        return max_sum


myobj = Solution()
inpt = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(myobj.maxSubArray(inpt))
