from typing import List
import math

"""
Problem Name: Search in Rotated Sorted Array

Problem Section: Sorting and Searching

Problem URL: https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem Difficulty: Medium


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
            
            # It implies that the left subarray nums[left ~ mid] is sorted. 
            # We can determine whether to proceed with this subarray by comparing target with the boundary elements
            if nums[mid] >= nums[left]:  # left rotated
                # in ascending order side. it suggests that the sorted left half might include target.
                # Consequently, we focus on the left half for further steps
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    # Otherwise, the left half is guaranteed not to contain target, and we will move on to the right half.
                    left = mid + 1
            # right rotated. It implies that the right subarray nums[mid ~ right] is sorted.
            # we can determine whether to proceed with the right subarray by comparing the target with its boundary elements
            else:
                # nums[mid] < nums[left]
                # in ascending order side.
                # it implies that the sorted right half might contain target. As a result, we will move on with the right half.
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    # Otherwise, the right half is guaranteed not to contain target, and we will move on to the left half.
                    right = mid - 1
        # cannot find the target value
        return -1


myobj = Solution()
# inpt = [4, 5, 6, 7, 0, 1, 2]
# target = 0
inpt = [1, 3]
target = 3
print(myobj.search(inpt, target))
