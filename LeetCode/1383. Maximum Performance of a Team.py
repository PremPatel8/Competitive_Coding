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

# Solution techniques are Greedy with Priority Queue

""" 
Greedy with Priority Queue

Time Complexity: O(nlogn+nlogk)

First, we build a list of candidates from the inputs, which takes O(N) time.
Sorting: Sorting the n candidates by efficiency takes O(nlogn).
Heap Operations: You iterate through the n candidates once. In each iteration, you perform heappush and potentially heappop. Since the heap size is maintained at a maximum of k elements, each heap operation takes O(logk). Over n iterations, this contributes O(nlogk).

Space Complexity: O(n+k)

Candidates List: Storing the zipped and sorted tuples of (efficiency, speed) takes O(n) space.
Heap: The speed_heap stores at most k elements, taking O(k) space.
Total: O(n) (since k≤n).
"""


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7

        # build tuples of (efficiency, speed)
        candidates = zip(efficiency, speed)
        # sort the candidates by their efficiencies, largest to smallest
        candidates = sorted(candidates, key=lambda t:t[0], reverse=True)

        speed_heap = []
        speed_sum, perf = 0, 0
        for curr_efficiency, curr_speed in candidates:
            # maintain a heap for the fastest (k-1) speeds
            if len(speed_heap) > k-1:
                # discard the team member with the lowest speed
                # This ensures that speed_sum always represents the sum of the largest speeds encountered so far for the given efficiency constraint.
                speed_sum -= heapq.heappop(speed_heap)
                
            heapq.heappush(speed_heap, curr_speed)

            # calculate the maximum performance with the current member as the least efficient one in the team
            speed_sum += curr_speed
            perf = max(perf, speed_sum * curr_efficiency)

        return perf % modulo


# class Solution:
#     def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
#         modulo = 10 ** 9 + 7
#         # people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
#         people = sorted(zip(efficiency, speed), reverse=True)

#         result, sum_speed = 0, 0
#         min_heap = []

#         for i, (e, s) in enumerate(people):
#             if i < k:
#                 sum_speed += s
#                 heapq.heappush(min_heap, s)
#             elif s > min_heap[0]:
#                 sum_speed += s - heapq.heappushpop(min_heap, s)

#             result = max(result, sum_speed * e)

#         return result % modulo

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
result = myobj.maxPerformance(n, speed, efficiency, k)
print(f"Expected = 72, Result = {result}, {72 == result}")
