from typing import List
import math

"""
Problem Name: 152. Maximum Product Subarray

Problem URL: https://leetcode.com/problems/maximum-product-subarray/

Problem Section: Array, DP

Problem Difficulty: Medium

Problem Statement:
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



Resources:
https://leetcode.com/problems/maximum-product-subarray/discuss/48276/Python-solution-with-detailed-explanation

runtime: 
187 / 187 test cases passed.
	Status: Accepted
Runtime: 56 ms
Memory Usage: 14.3 MB
"""



""" 
Dynamic Programming

Solution techniques are DP, Kadane's algo with both min product so far and max product so far
since multiplying two negatives gives you a positive, we have to track both the min prouct till i-1 and max product till i-1
then max prod at index i is max(nums[i], maxProd[i-1]*nums[i], minProd[i-1]*nums[i])
To make it constant space, we can use two variables to track minProd and maxProd so far instead of two DP arrays

Time complexity : O(N) where N is the size of nums. The algorithm achieves linear runtime since we are going through nums only once.

Space complexity : O(1) since no additional space is consumed rather than variables which keep track of the maximum product so far, the minimum product so far, current variable, temp variable, and placeholder variable for the result.

"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = min_so_far = result = nums[0]

        for idx in range(1, len(nums)):
            curr_no = nums[idx]
            temp_max_so_far = max(curr_no, max(max_so_far * curr_no, min_so_far * curr_no))
            temp_min_so_far = min(curr_no, min(max_so_far * curr_no, min_so_far * curr_no))

            max_so_far = temp_max_so_far
            min_so_far = temp_min_so_far

            # Update the result with the maximum product found so far
            result = max(max_so_far, result)

        return result




"""
Brute Force TLE

Time complexity : O(N2) where N is the size of nums. Since we are checking every possible contiguous subarray following every element in nums we have quadratic runtime.

Space complexity : O(1) since we are not consuming additional space other than two variables: result to hold the final result and accu to accumulate product of preceding contiguous subarrays.

"""

class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)

        return result

myobj = Solution()
inpt = [2, 3, -2, 4]
print(myobj.maxProduct(inpt))
