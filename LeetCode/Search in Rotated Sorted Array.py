from typing import List
import math

"""
Problem Name: Search in Rotated Sorted Array

Problem Section: Sorting and Searching

Problem Statement:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

""" 196 / 196 test cases passed.
	Status: Accepted
Runtime: 48 ms
Memory Usage: 14 MB """

# Time complexity : O(n log⁡ n) Space complexity : O(1) Binary search solution with infinity


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (right-left)//2 + left

            comparator = nums[mid]

            if ((target >= nums[0]) == (nums[mid] >= nums[0])):
                comparator = nums[mid]
            elif target < nums[0]:
                comparator = -math.inf
            else:
                comparator = math.inf

            if comparator == target:
                return mid

            if target > comparator:
                left = mid+1
            else:
                right = mid-1

        return -1


myobj = Solution()
# inpt = [4, 5, 6, 7, 0, 1, 2]
# target = 0
inpt = [1,3]
target = 3
print(myobj.search(inpt, target))
