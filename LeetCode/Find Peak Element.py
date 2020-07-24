from typing import List

"""
Problem Name: Find Peak Element

Problem Section: Sorting and Searching

Problem Statement:
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Follow up: Your solution should be in logarithmic complexity.
"""

""" 59 / 59 test cases passed.
	Status: Accepted
Runtime: 52 ms
Memory Usage: 13.8 MB """

# Time complexity : O(n), Space complexity : O(1) Linear solution


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i

        return len(nums)-1


myobj = Solution()
inpt = [1, 2]
print(myobj.findPeakElement(inpt))
