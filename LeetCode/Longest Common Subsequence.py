from functools import lru_cache
from typing import List

"""
Problem Name: Longest Common Subsequence

Problem URL: https://leetcode.com/problems/longest-common-subsequence/

Problem Section: Recursion, Dynamic Programming

Problem Difficulty: Medium

Problem Statement:
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.


Resources:

"""


class Solution:
    """
    Solution technique: Dynamic Programming

    Time & Space Complexity:
    Time: O(M * N)
    we are solving M * N subproblems. Solving each subproblem is O(1) operation
    Space: O(M * N)
    We are allocating a 2D array of size M * N to save the answers to the subproblems

    Runtime:
    44 / 44 test cases passed.
        Status: Accepted
    Runtime: 360 ms
    Memory Usage: 22 MB
    """
    # DP in reverse, from bottom right to top left
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:

    #     # Make a grid of 0's with len(text2) + 1 columns
    #     # and len(text1) + 1 rows.
    #     dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    #     # Iterate up each column, starting from the last one.
    #     for col in reversed(range(len(text2))):
    #         for row in reversed(range(len(text1))):
    #             # If the corresponding characters for this cell are the same...
    #             if text2[col] == text1[row]:
    #                 dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
    #             # Otherwise they must be different...
    #             else:
    #                 dp_grid[row][col] = max(
    #                     dp_grid[row + 1][col], dp_grid[row][col + 1])

    #     # The original problem's answer is in dp_grid[0][0]. Return it.
    #     return dp_grid[0][0]

    # normal DP, top left to bottom right
    # text1 == Rows
    # text2 == Columns
    """ 44 / 44 test cases passed.
            Status: Accepted
        Runtime: 388 ms
        Memory Usage: 21.9 MB """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Make a grid of 0's with len(text2) + 1 columns
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # Iterate up each column, starting from the last one.
        for row in range(len(text1)):
            for col in range(len(text2)):
                # If the corresponding characters for this cell are the same...
                if text1[row] == text2[col]:
                    dp_grid[row+1][col+1] = 1 + dp_grid[row][col]
                # Otherwise they must be different...
                else:
                    dp_grid[row+1][col +
                                   1] = max(dp_grid[row][col+1], dp_grid[row+1][col])

        # The original problem's answer is in dp_grid[-1][-1]. Return it.
        return dp_grid[-1][-1]


"""
Solution technique: Recursion with memoization

Time & Space Complexity:
Time: O(M * N)
we are solving M * N subproblems. Solving each subproblem is O(1) operation
Space: O(M * N)
We are allocating a 2D array of size M * N to save the answers to the subproblems
"""


# class Solution:
""" Runtime:
        44 / 44 test cases passed.
            Status: Accepted
        Runtime: 784 ms
        Memory Usage: 141.8 MB """
# def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#     @lru_cache(maxsize=None)
#     def memo_solve(p1, p2):

#         # Base case: If either string is now empty, we can't match
#         # up anymore characters.
#         if p1 == len(text1) or p2 == len(text2):
#             return 0

#         # Recursive case 1.
#         if text1[p1] == text2[p2]:
#             return 1 + memo_solve(p1 + 1, p2 + 1)

#         # Recursive case 2.
#         else:
#             return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

#     return memo_solve(0, 0)

# Sol without lru cache, instead using memo grid/matrix/2D array
# text1 == Rows
# text2 == Columns
""" 44 / 44 test cases passed.
            Status: Accepted
        Runtime: 644 ms
        Memory Usage: 24.7 MB """

# def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#     memo = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

#     for i in range((len(text1) + 1)):
#         j = len(text2)
#         memo[i][j] = 0

#     for j in range((len(text2) + 1)):
#         i = len(text1)
#         memo[i][j] = 0

#     def memo_solve(p1, p2):

#         # Check whether or not we've already solved this subproblem.
#         # This also covers the base cases where p1 == text1.length
#         # or p2 == text2.length.
#         if memo[p1][p2] != -1:
#             return memo[p1][p2]

#         res = 0
#         # Recursive case 1.
#         if text1[p1] == text2[p2]:
#             res = 1 + memo_solve(p1 + 1, p2 + 1)

#         # Recursive case 2.
#         else:
#             res = max(memo_solve(p1, p2 + 1),
#                       memo_solve(p1 + 1, p2))

#         memo[p1][p2] = res
#         return memo[p1][p2]

#     return memo_solve(0, 0)


myobj = Solution()
text1 = "abcde"
text2 = "ace"
# Output: 3
print(myobj.longestCommonSubsequence(text1, text2))

"""
import file_name
def test_name():
    assert file_name.Solution().functionName(val) == OP
"""
