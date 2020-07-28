from typing import List

"""
Problem Name: Unique Paths

Problem Section: Dynamic Programming

Problem Statement:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?


Example:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Input: m = 7, n = 3
Output: 28

Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""

""" 62 / 62 test cases passed.
	Status: Accepted
Runtime: 40 ms
Memory Usage: 14 MB """

# Time complexity : O() Space complexity : O() DP Bottom Up solution


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n<=0:
            return 0
        if m == 1 and n == 1:
            return 1

        dp_array = [[1 for _ in range(n)] for _ in range(m)]

        print(dp_array)

        for i in range(1, m):
            for j in range(1, n):
                dp_array[i][j] = dp_array[i][j-1]+dp_array[i-1][j]

        return dp_array[-1][-1]


myobj = Solution()
# m = 3
# n = 2
m = 7
n = 3
print(myobj.uniquePaths(m, n))
