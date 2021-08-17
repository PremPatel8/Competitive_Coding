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

# Solution techniques are DP, Kadane's algo with both min product so far and max product so far
# since multiplying two negatives gives you a positive, we have to track both the min prouct till i-1 and max product till i-1
# then max prod at index i is max(nums[i], maxProd[i-1]*nums[i], minProd[i-1]*nums[i])
# To make it constant space, we can use two variables to track minProd and maxProd so far instead of two DP arrays

# Time complexity : O(n) Space complexity : O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = maxProd = minProd = nums[0]

        for num in nums[1:]:
            tempMaxProd = max(num, maxProd*num, minProd*num)
            tempMinProd = min(num, maxProd*num, minProd*num)

            maxProd = tempMaxProd
            minProd = tempMinProd

            ans = max(ans, maxProd)

        return ans


myobj = Solution()
inpt = [2, 3, -2, 4]
print(myobj.maxProduct(inpt))
