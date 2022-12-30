from typing import List

"""
Problem Name: Find Pivot Index

Problem URL: https://leetcode.com/problems/find-pivot-index/description/

Problem Section: Array, Prefix Sum

Problem Difficulty: Easy

Problem Statement:
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Resources:

"""


class Solution:
    """
    Solution technique: Iterate through the array and calculate lsum by adding the encountered values,
    rsum at each point is totalSum-lsum-currNo

    Time & Space Complexity:
    Time: O(n)
    Space: O(1)

    Runtime: 334 ms
    Memory: 15.4 MB

    """

    def pivotIndex(self, nums: List[int]) -> int:
        res = -1
        totalSum = sum(nums)
        lsum = 0

        for idx, no in enumerate(nums):
            rsum = totalSum-lsum-no

            if lsum == rsum:
                return idx

            lsum += no

        return res


myobj = Solution()
inpt = [1,7,3,6,5,6]
opt = 3
print(myobj.pivotIndex(inpt) == opt)

"""
import file_name
def test_name():
    assert file_name.Solution().functionName(val) == OP
"""
