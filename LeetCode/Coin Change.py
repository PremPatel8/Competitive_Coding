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
Runtime: 1872 ms
Memory Usage: 17.1 MB """
# Alternate solution techniques are DFS, DP table, DP Top Down(memoization)

# Time complexity : O(S*n) Space complexity : O(S) Dynamic programming - Top down (memoization) solution
# S = amount, n = number of coin denomination count


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0

        def coinChange(coins, rem, count):
            if rem < 0:
                return -1

            if rem == 0:
                return 0

            if count[rem-1] != 0:
                return count[rem-1]

            minval = float('inf')

            for coin in coins:
                res = coinChange(coins, rem-coin, count)

                if res >= 0 and res < minval:
                    minval = 1+res

            count[rem-1] = minval if minval != float('inf') else -1
            return count[rem - 1]

        return coinChange(coins, amount, [0]*amount)


myobj = Solution()
coins = [1, 2, 5]
amount = 11
print(myobj.coinChange(coins, amount))
