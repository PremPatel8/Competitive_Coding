from typing import List
import math

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

Resources:
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/discuss/22954/C++-DP
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/discuss/23234/Accpeted-simple-Python-DP-solution.
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/discuss/22975/Python-easy-to-understand-solutions-(math-dp-O(m*n)-and-O(n)-space).
http://www.crazyforcode.com/paths-rectangular-grid/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/discuss/22958/Math-solution-O(1)-space
"""

""" 62 / 62 test cases passed.
	Status: Accepted
Runtime: 60 ms
Memory Usage: 13.8 MB """

# Time complexity : O() Space complexity : O() Math Permutation Factorial solution


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0

        return math.factorial((m-1)+(n-1))//(math.factorial(m-1)*math.factorial(n-1))


myobj = Solution()
# m = 3
# n = 2
m = 7
n = 3
print(myobj.uniquePaths(m, n))
