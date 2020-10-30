from typing import List

"""
Problem Name: 64. Minimum Path Sum

Problem URL: https://leetcode.com/problems/minimum-path-sum/

Problem Section: 

Problem Statement:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.



Resources:

runtime: 
61 / 61 test cases passed.
	Status: Accepted
Runtime: 92 ms
Memory Usage: 15.4 MB
"""

# Solution techniques are Optimized DP, resusing input grid to save space

# Time complexity : O(nm) Space complexity : O(1)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        for r in range(rows):
            for c in range(columns):
                if r > 0 and c > 0:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                elif r > 0:
                    grid[r][c] += grid[r-1][c]
                elif c > 0:
                    grid[r][c] += grid[r][c-1]

        return grid[-1][-1]


myobj = Solution()
inpt = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(myobj.minPathSum(inpt))
