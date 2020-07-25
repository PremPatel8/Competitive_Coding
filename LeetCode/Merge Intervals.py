from typing import List

"""
Problem Name: Merge Intervals

Problem Section: Sorting and Searching

Problem Statement:
Given a collection of intervals, merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

""" 169 / 169 test cases passed.
	Status: Accepted
Runtime: 108 ms
Memory Usage: 15.5 MB """

# Time complexity : O(n log⁡ n) Space complexity : O(1) Sorting solution


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or
            # if the current interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


myobj = Solution()
# inpt = [[1, 3], [2, 6], [8, 10], [15, 18]]
# inpt = [[1, 4], [0, 4]]
# inpt = [[1, 4], [0, 1]]
# inpt = [[1, 4], [1, 4]]
# inpt = [[1, 4], [2, 3]]
inpt = [[1, 4], [0, 0]]
print(myobj.merge(inpt))
