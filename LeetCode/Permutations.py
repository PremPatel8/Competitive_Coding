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
        output = []

        if not nums or len(nums) == 0:
            return output

        def backtrack(permutation, nums):
            if len(permutation) == len(nums):
                output.append(permutation.copy())
            else:
                for num in nums:
                    if num in permutation:
                        continue

                    permutation.append(num)
                    backtrack(permutation, nums)
                    permutation.pop()

        backtrack([], nums)

        return output


myobj = Solution()

print(myobj.permute([1, 2, 3]))
