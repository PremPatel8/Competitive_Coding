from typing import List
import heapq

"""
Problem Name: 1383. Maximum Performance of a Team

Problem Section: Greedy, Sort, min head / priority queue

Problem Statement:
There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

Example 1:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.


Resources:
https://leetcode.com/problems/maximum-performance-of-a-team/discuss/741822/Met-this-problem-in-my-interview!!!-(Python3-greedy-with-heap)
https://leetcode.com/problems/maximum-performance-of-a-team/discuss/539687/JavaC%2B%2BPython-Priority-Queue
"""

""" 53 / 53 test cases passed.
	Status: Accepted
Runtime: 384 ms
Memory Usage: 29.8 MB """

# Solution techniques are Sort based on efficiency, use min heap to store k element speeds and to pop elements with speed less than curr element speed and calculate running best speed for curr element efficiency

# Time complexity : O(n log n)? Space complexity : O(k)


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        people = sorted(zip(efficiency, speed), reverse=True)

        result, sum_speed = 0, 0
        min_heap = []

        for i, (e, s) in enumerate(people):
            if i < k:
                sum_speed += s
                heapq.heappush(min_heap, s)
            elif s > min_heap[0]:
                sum_speed += s - heapq.heappushpop(min_heap, s)

            result = max(result, sum_speed * e)

        return result % ((10**9)+7)

        """ def maxPerformance(self, n, speed, efficiency, k):
        h = []
        res = sSum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(h, s)
            sSum += s
            if len(h) > k:
                sSum -= heapq.heappop(h)
            res = max(res, sSum * e)
        return res % (10**9 + 7) """


myobj = Solution()
n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 4
print(myobj.maxPerformance(n, speed, efficiency, k))
