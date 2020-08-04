from typing import List

"""
Problem Name: Best Time to Buy and Sell Stock II

Problem Section: Array

Problem Statement:
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Constraints:
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

Resources:

"""

""" 200 / 200 test cases passed.
	Status: Accepted
Runtime: 64 ms
Memory Usage: 14.8 MB """

# Solution technique is iterating through the prices and adding positive deltas to the profit

# Time complexity : O(n) Space complexity : O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for itr in range(1, len(prices)):
            profit += max(0, prices[itr]-prices[itr-1])

        return profit


myobj = Solution()
# inpt = [7, 1, 5, 3, 6, 4]
# inpt = [1, 2, 3, 4, 5]
# inpt = [7, 6, 4, 3, 1]
# inpt = [6, 1, 3, 2, 4, 7]
inpt = [1, 4, 2]

print(myobj.maxProfit(inpt))
