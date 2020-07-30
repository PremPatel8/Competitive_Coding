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
Runtime: 204 ms
Memory Usage: 13.9 MB """
# Alternate solution techniques are BFS, DFS, DP table (Bottom Up), DP Top Down (memoization)

# Time complexity : O() Space complexity : O() DFS recursive solution
# S = amount, n = number of coin denomination count


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        min_coins = float('inf')

        def count_coins(start_coin, coin_count, remaining_amount):
            nonlocal min_coins

            if remaining_amount == 0:
                min_coins = min(min_coins, coin_count)
                return

            # Iterate from largest coins to smallest coins
            for i in range(start_coin, len(coins)):
                remaining_coin_allowance = min_coins - coin_count
                max_amount_possible = coins[i] * remaining_coin_allowance

                if coins[i] <= remaining_amount and remaining_amount < max_amount_possible:
                    count_coins(i, coin_count + 1, remaining_amount - coins[i])

        count_coins(0, 0, amount)

        return min_coins if min_coins < float('inf') else -1


myobj = Solution()
# coins = [1, 2, 5]
# amount = 11
coins = [1, 2, 3]
amount = 6
print(myobj.coinChange(coins, amount))


"""
# Alternate DFS Recursive
def coinChange(coins, amount):
    m = 2**31 - 1

    def coinChangeHelper(index, amount, count):
        nonlocal m, coins

        if amount == 0:
            m = min(m, count)

        for j in range(index, len(coins), 1):
            if coins[j] <= amount < (m - count)*coins[j]:  # most important line
                n = amount//coins[j]
                i = n
                while i > 0:
                    if amount - i * coins[j] < (m - count - i)*coins[j]: # most important line
                        coinChangeHelper(j+1, amount - i*coins[j], count + i)
                    else:
                        break
                    i -= 1


    coins.sort(reverse = True)
    coinChangeHelper(0, amount, 0)
    return m if m < 2**31 - 1 else -1 
"""

""" 
   #  DFS Iterative
    class Solution:
       def coinChange(self, coins, amount):
           coins.sort()
           stack = [(0, 0, len(coins))] # steps, accumulated
           min_steps = 2**31

           while len(stack) != 0:
               steps, accumulated, sequence = stack.pop()

               if accumulated == amount:
                   min_steps = min(min_steps, steps)

               if accumulated > amount or amount - accumulated > coins[sequence-1] * (min_steps-steps):
                   continue

               for seq, coin in enumerate(coins[:sequence]):
                   stack.append((steps+1, accumulated+coin, seq+1))

           return min_steps if min_steps != 2**31 else -1
"""
