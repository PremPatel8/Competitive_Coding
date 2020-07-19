from typing import List

"""
Problem Name: Permutations

Problem Section: Backtracking

Problem Statement: 
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        l = []
        for i in range(len(nums)):
            m = nums[i]
            rem = nums[:i]+nums[i+1:]
            for p in self.permute(rem):
                l.append([m]+p)
        return l


myobj = Solution()

print(myobj.permute([1, 2, 3]))
