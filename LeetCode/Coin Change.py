from typing import List

"""
Problem Name: Coin Change

Problem Section: Dynamic Programming

Problem Statement:
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.


Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.

Resources:
https://leetcode.com/articles/coin-change/#
"""

""" 182 / 182 test cases passed.
	Status: Accepted
Runtime: 1536 ms
Memory Usage: 13.9 MB """

# Time complexity : O(S*n) Space complexity : O(S) Dynamic programming - Bottom up solution
# S = amount, n = number of coin denomination count


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


myobj = Solution()
coins = [1, 2, 5]
amount = 11
print(myobj.coinChange(coins, amount))
