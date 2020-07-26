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
Runtime: 60 ms
Memory Usage: 13.9 MB """

# Time complexity : O(log⁡ n) Space complexity : O(1) Binary search solution without infinity


class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (right-left)//2 + left

            # if found target value, return the index
            if nums[mid] == target:
                return mid

            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid
                 
            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
            
            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[left]:  # left rotated
                # in ascending order side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right rotated
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1


myobj = Solution()
# inpt = [4, 5, 6, 7, 0, 1, 2]
# target = 0
inpt = [1, 3]
target = 3
print(myobj.search(inpt, target))
