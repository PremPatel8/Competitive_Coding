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
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     coins.sort(reverse=True)
    #     min_coins = float('inf')

    #     def count_coins(start_coin, coin_count, remaining_amount):
    #         nonlocal min_coins

    #         if remaining_amount == 0:
    #             min_coins = min(min_coins, coin_count)
    #             return

    #         # Iterate from largest coins to smallest coins
    #         for i in range(start_coin, len(coins)):
    #             remaining_coin_allowance = min_coins - coin_count
    #             max_amount_possible = coins[i] * remaining_coin_allowance

    #             if coins[i] <= remaining_amount and remaining_amount < max_amount_possible:
    #                 count_coins(i, coin_count + 1, remaining_amount - coins[i])

    #     count_coins(0, 0, amount)

    #     return min_coins if min_coins < float('inf') else -1

    """ 
    Dynamic programming - Top down / Recursive + memo
    Recursion Tree visualization for Coin Change - https://visualgo.net/en/recursion

    Time complexity : O(S∗n). where S is the amount, n is denomination count. In the worst case the recursive tree of the algorithm has height of S and the algorithm solves only S subproblems because it caches precalculated solutions in a table. Each subproblem is computed with n iterations, one by coin denomination. Therefore there is O(S∗n) time complexity.

    Space complexity : O(S), where S is the amount to change We use extra space for the memoization table.

    Runtime - 1728 ms
    Memory Usage - 20 MB

    """

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     if amount < 1:
    #         return 0

    #     def coinChange(coins, rem, count):
    #         if rem < 0:
    #             return -1

    #         if rem == 0:
    #             return 0

    #         if count[rem-1] != 0:
    #             return count[rem-1]

    #         minval = float('inf')

    #         for coin in coins:
    #             res = coinChange(coins, rem-coin, count)

    #             if res >= 0 and res < minval:
    #                 minval = 1+res

    #         count[rem-1] = minval if minval != float('inf') else -1
    #         return count[rem - 1]

    #     return coinChange(coins, amount, [0]*amount)

    """ 
    Dynamic programming - Bottom up / Iterative

    same time & space complexity as Top Down DP

    Runtime: 1176 ms
    Memory Usage: 14.4 MB

    Input: coins = [1,2,3], amount = 6
    Output: 2
    Explanation: 6 = 3 + 3

    Coin = 1, x = [1,2,3,4,5,6]
    dp[1] = min(dp[1], dp[0]+1)
    dp[2] = min(dp[2], dp[1]+1)
    dp[3] = min(dp[3], dp[2]+1)
    dp[4] = min(dp[4], dp[3]+1)
    dp[5] = min(dp[5], dp[4]+1)
    dp[6] = min(dp[6], dp[5]+1)


    Coin = 2, x = [2,3,4,5,6]
    dp[2] = min(dp[2], dp[0]+1)
    dp[3] = min(dp[3], dp[1]+1)
    dp[4] = min(dp[4], dp[2]+1)
    dp[5] = min(dp[5], dp[3]+1)
    dp[6] = min(dp[6], dp[4]+1)


    Coin = 3, x = [3,4,5,6]
    dp[3] = min(dp[3], dp[0]+1)
    dp[4] = min(dp[4], dp[1]+1)
    dp[5] = min(dp[5], dp[2]+1)
    dp[6] = min(dp[6], dp[3]+1)

    for each amount the min number of coins is the overall minimmum of the min number of coins needed for amt-c1, amt-c2, amtc3 ....
    for example dp[6] = min(dp[5], dp[4], dp[3]) if there were 3 coins [1,2,3] and amount needed was 6

    For the iterative solution, we think in bottom-up manner. Before calculating F(i), we have to compute all minimum counts for amounts up to i. On each iteration i of the algorithm F(i) is computed as min⁡j=0…n−1 F(i−cj)+1

    """

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [float('inf')] * (amount + 1)
    #     dp[0] = 0

    #     for coin in coins:
    #         for amt in range(coin, amount + 1):
    #             dp[amt] = min(dp[amt], dp[amt - coin] + 1)
    #     return dp[amount] if dp[amount] != float('inf') else -1

    
    """ 
    Iterative BFS Solution Optimimum
    find the shortet path from 0 to required amount.

    Runtime: 640 ms
    Memory Usage: 14.3 MB
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Use BFS which is to find the shortest path from 0 to amount.
        This is much faster than the above dp solution.
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
# coins = [1, 2, 5]
# amount = 11
coins = [1, 2, 3]
amount = 6
print(myobj.coinChange(coins, amount))


"""
# Alternate DFS Recursive TLE
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
   #  DFS Iterative TLE
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
