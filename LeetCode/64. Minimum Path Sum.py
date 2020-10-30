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
Runtime: 96 ms
Memory Usage: 15.4 MB
"""

# Solution techniques are DP

# Time complexity : O(nm) Space complexity : O(nm)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        dp = [[0 for _ in range(columns)] for _ in range(rows)]

        for r in range(rows):
            for c in range(columns):
                dp[r][c] += grid[r][c]

                if r > 0 and c > 0:
                    dp[r][c] += min(dp[r-1][c], dp[r][c-1])
                elif r > 0:
                    dp[r][c] += dp[r-1][c]
                elif c > 0:
                    dp[r][c] += dp[r][c-1]

        return dp[-1][-1]


myobj = Solution()
inpt = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(myobj.minPathSum(inpt))
