from typing import List

"""
Problem Name: Best Time to Buy and Sell Stock

Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem Section: Dynamic Programming

Problem Statement:
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Resources:

"""
""" 200 / 200 test cases passed.
	Status: Accepted
Runtime: 60 ms
Memory Usage: 14.9 MB """

# Solution techniques are Dynamic Programming:
# the max profit possible by selling a stock on day i is the difference between price on day i and smallest price seen before day i
# find the min price seen so far till index i, by using DP to keep track of min price at each index i-1
# We can use a DP array (Linear Space) to store the min price till each index i
# Then we can use the following formula to calculate min price at i:
# min_price[i] = min(price[i], min_price[i-1])
# We can also convert it to (constant space) DP by storing the last min price in the min_price variable, as we only need the smallest value till the last index
# calculate the profit by subtracting min price so far from price at i,
# update max_profit if it's less than profit generated at price i
# Time complexity : O(n) Space complexity : O(1) Iterative Greedy pythonic solution
""" 
Complexity Analysis
Time complexity : O(n) Only a single pass is needed.
Space complexity : O(1) Only two variables are used.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


myobj = Solution()
inpt = [7, 1, 5, 3, 6, 4]
print(f"{myobj.maxProfit(inpt)} == 5 => {myobj.maxProfit(inpt)==5}")
