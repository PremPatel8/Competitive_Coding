from typing import List

"""
Problem Name: Best Time to Buy and Sell Stock II

Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Problem Section: Array, DP, Greedy

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
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/discuss/39404/Shortest-and-fastest-solution-with-explanation.-You-can-never-beat-this.
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/discuss/208241/Explanation-for-the-dummy-like-me.
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/discuss/39531/Java-O(n)-solution-if-we're-not-greedy
"""

""" 200 / 200 test cases passed.
	Status: Accepted
Runtime: 64 ms
Memory Usage: 14.8 MB """

# Solution technique is iterating through the prices and adding positive deltas to the profit

""" 
instead of looking for every peak following a valley, we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction. 
In the end,we will be using the peaks and valleys effectively, but we need not track the costs corresponding to the peaks and valleys along with the maximum profit, 
but we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one, 
and at the total sum we obtain will be the maximum profit.
"""

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


""" 
# Alt solution Peak Valley Approach

If we analyze the graph, we notice that the points of interest are the consecutive valleys and peaks.

Mathematically speaking: TotalProfit=∑i(height(peaki)−height(valleyi)) Total Profit= \sum_{i}(height(peak_i)-height(valley_i)) TotalProfit=∑i​(height(peaki​)−height(valleyi​))

The key point is we need to consider every peak immediately following a valley to maximize the profit. In case we skip one of the peaks (trying to obtain more profit), we will end up losing the profit over one of the transactions leading to an overall lesser profit.

For example, in the above case, if we skip peakipeak_ipeaki​ and valleyjvalley_jvalleyj​ trying to obtain more profit by considering points with more difference in heights, the net profit obtained will always be lesser than the one obtained by including them, since CCC will always be lesser than A+BA+BA+B.

class Solution {
    public int maxProfit(int[] prices) {
        int i = 0;
        int valley = prices[0];
        int peak = prices[0];
        int maxprofit = 0;
        while (i < prices.length - 1) {
            while (i < prices.length - 1 && prices[i] >= prices[i + 1])
                i++;
            valley = prices[i];
            while (i < prices.length - 1 && prices[i] <= prices[i + 1])
                i++;
            peak = prices[i];
            maxprofit += peak - valley;
        }
        return maxprofit;
    }
}

class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}
"""
