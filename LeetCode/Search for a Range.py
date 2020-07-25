from typing import List

"""
Problem Name: Search for a Range

Problem Section: Sorting and Searching

Problem Statement:
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
"""

""" 88 / 88 test cases passed.
	Status: Accepted
Runtime: 92 ms
Memory Usage: 15.3 MB """

# Time complexity : O(log⁡ n) Space complexity : O(1) Binary Search solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)]

    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.

    def extreme_insertion_index(self, nums, target, leftFlag):
        index = -1
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target or (leftFlag and nums[mid] == target):
                right = mid-1
            else:
                left = mid+1

            if nums[mid] == target:
                index = mid

        return index


myobj = Solution()
inpt = [5, 7, 7, 8, 8, 10]
# target = 8
target = 6
print(myobj.searchRange(inpt, target))
