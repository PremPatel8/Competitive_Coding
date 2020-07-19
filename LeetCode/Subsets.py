from typing import List

"""
Problem Name: Subsets

Problem Section: Backtracking

Problem Statement:
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(temp, nums, output, start):
            output.append(temp.copy())

            i = start
            while i < len(nums):
                temp.append(nums[i])
                backtrack(temp, nums, output, i+1)
                temp.pop()
                i += 1

        if nums:
            backtrack([], nums, output, 0)

        return output


myobj = Solution()

print(myobj.subsets([1, 2, 3]))
