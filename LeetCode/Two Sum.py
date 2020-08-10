from typing import List
from collections import Counter
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
""" 29 / 29 test cases passed.
	Status: Accepted
Runtime: 44 ms
Memory Usage: 15.3 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(n) Optimized One-pass Hash Table / Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        if not nums or len(nums) == 0:
            return res

        if len(nums) == 2:
            if (nums[0]+nums[1]) == target:
                res = [0, 1]
            return res

        numIndex = dict()

        for i, no in enumerate(nums):
            complement = target-no

            if complement in numIndex:
                res = [numIndex[complement], i]
                break

            numIndex[no] = i

        return res


myobj = Solution()
nums = [2, 7, 11, 15]
target = 9
print(myobj.twoSum(nums, target))


# %%
