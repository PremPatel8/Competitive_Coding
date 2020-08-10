from typing import List
"""
Problem Name: Move Zeroes

Problem Section: Array

Problem Statement:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Resources:
"""
""" 21 / 21 test cases passed.
	Status: Accepted
Runtime: 48 ms
Memory Usage: 15 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(1) time and space optimized two pointer(slow & fast) solution


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1 or not nums:
            return

        lastNonZero = 0

        for itr in range(len(nums)):
            if nums[itr] != 0:
                nums[lastNonZero], nums[itr] = nums[itr], nums[lastNonZero]
                lastNonZero += 1


myobj = Solution()
inpt = [0, 1, 0, 3, 12]
print(myobj.moveZeroes(inpt))
