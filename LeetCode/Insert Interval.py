import heapq
from typing import List

"""
Problem Name: Insert Interval

Problem URL: https://leetcode.com/problems/insert-interval/description/

Problem Section:

Problem Difficulty: Medium

Problem Statement:
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

Resources:

"""


class Solution:
    """
    Solution technique: Heap

    Time & Space Complexity:

    Runtime:
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heap = []
        result = []

        # add start & end to heap (-1 is start, 1 is end)
        for interval_start, interval_end in intervals + [newInterval]:
            heapq.heappush(heap, (interval_start, -1))
            heapq.heappush(heap, (interval_end, 1))

        cur = 0
        start = None

        # print(heap)

        while heap:
            interval_no, val = heapq.heappop(heap)       # pop heap
            # print(f"interval_no = {interval_no}, val = {val}")

            if start is None:
                # is start is None, assign interval_no to start (interval start)
                start = interval_no

            cur += val                         # keep counting until close interval

            if cur == 0:                        # when cur == 0, meaning we can close the interval
                # append interval to result
                result.append([start, interval_no])
                start = None                       # reset s to None

        return result

    """
    Solution technique: array traversal

    Time & Space Complexity:

    Runtime:
    """

    def insert_1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for idx, curr_interval in enumerate(intervals):
            # the new interval is before the curr_interval, so we can add the new interval and append the remaining intervals directly as they are already sorted
            if newInterval[1] < curr_interval[0]:
                result.append(newInterval)
                # newInterval = curr_interval
                return result + intervals[idx:]

            # the new interval is after the of curr_interval, so we can leave the current interval as is because the new one does not overlap with it
            elif newInterval[0] > curr_interval[1]:
                result.append(curr_interval)

            # the new interval overlaps the curr_interval, so we must choose the min for start and max for end of interval
            else:
                newInterval[0] = min(newInterval[0], curr_interval[0])
                newInterval[1] = max(newInterval[1], curr_interval[1])

        result.append(newInterval)

        return result


myobj = Solution()

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

# print(myobj.insert(intervals, newInterval))
print(myobj.insert_1(intervals, newInterval))

"""
import file_name
def test_name():
    assert file_name.Solution().functionName(val) == OP
"""
