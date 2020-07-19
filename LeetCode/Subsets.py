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

# Iterative solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for ele in nums:
            result += [entry + [ele] for entry in result]
        return result


myobj = Solution()

print(myobj.subsets([1, 2, 3]))
