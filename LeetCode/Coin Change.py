from typing import List
from collections import deque

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
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/809/discuss/77361/Fast-Python-BFS-Solution
"""

""" 182 / 182 test cases passed.
	Status: Accepted
Runtime: 820 ms
Memory Usage: 13.9 MB """
# Alternate solution techniques are BFS, DP table Bottom Up, DP Top Down(memoization)

# Time complexity : O(S*n) Space complexity : O(S) BFS solution
# S = amount, n = number of coin denomination count


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Use BFS which is to find the shortest path from 0 to amount.
        This is much faster than the dp solution.
        """
        if not amount:  # Don't need any coin.
            return 0

        queue = deque([(0, 0)])
        visited = [True] + [False] * amount
        while queue:
            totalCoins, currVal = queue.popleft()
            totalCoins += 1  # Take a new coin.
            for coin in coins:
                nextVal = currVal + coin
                if nextVal == amount:  # Find a combination.
                    return totalCoins

                if nextVal < amount:  # Could add more coins.
                    if not visited[nextVal]:  # Current value not checked.
                        visited[nextVal] = True  # Prevent checking again.
                        queue.append((totalCoins, nextVal))

        return -1  # Cannot find any combination.


myobj = Solution()
coins = [1, 2, 5]
amount = 11
coins = [1, 2, 3]
amount = 6
print(myobj.coinChange(coins, amount))
