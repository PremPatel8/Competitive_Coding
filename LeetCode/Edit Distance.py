from typing import List

"""
Problem Name: 72. Edit Distance

Problem URL: https://leetcode.com/problems/edit-distance/

Problem Section: DP, string

Problem Difficulty: Hard

Problem Statement:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character

 

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')


Resources:

"""


class Solution:
    """
    Solution technique: bottom up dynamic programming

    Time & Space Complexity:
    Time - O(mn)
    Space - O(mn)

    Runtime:
    1146 / 1146 test cases passed.
        Status: Accepted
    Runtime: 180 ms
    Memory Usage: 17.9 MB
    """

    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)

        if not word1 or not word2:
            if not word1:
                return word2_len
            elif not word2:
                return word1_len

        dp = [[0 for _ in range(word2_len+1)] for _ in range(word1_len+1)]

        for i in range(word1_len+1):
            dp[i][0] = i

        for j in range(word2_len+1):
            dp[0][j] = j

        for i in range(1, word1_len+1):
            for j in range(1, word2_len+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

        return dp[-1][-1]


myobj = Solution()
word1 = "distance"
word2 = "springbok"
print(myobj.minDistance(word1, word2))

"""
import file_name
def test_name():
    assert file_name.Solution().functionName(val) == OP
"""
