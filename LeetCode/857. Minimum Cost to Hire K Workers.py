from typing import List

"""
Problem Name: 857. Minimum Cost to Hire K Workers

Problem URL: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

Problem Section: Greedy, Sort, min head / priority queue

Problem Statement:
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:
    Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
    Every worker in the paid group must be paid at least their minimum wage expectation.

Return the least amount of money needed to form a paid group satisfying the above conditions.

Example 1:
Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

Note:
1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.

Resources:

"""

""" runtime """

# Solution techniques are

# Time complexity : O() Space complexity : O()


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        pass


myobj = Solution()
quality = [10, 20, 5]
wage = [70, 50, 30]
K = 2
print(myobj.mincostToHireWorkers(quality, wage, K))
