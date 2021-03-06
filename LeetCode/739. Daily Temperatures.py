from typing import List

"""
Problem Name: 739. Daily Temperatures

Problem URL: https://leetcode.com/problems/daily-temperatures/

Problem Section: 

Problem Statement:
 Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]. 

Resources:
https://leetcode.com/problems/daily-temperatures/discuss/397728/Easy-Python-O(n)-time-O(1)-space-beat-99.9

runtime: 
38 / 38 test cases passed.
	Status: Accepted
Runtime: 480 ms
Memory Usage: 18.5 MB
"""

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n) Optimized Stack solution


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        seen_stack = []
        res = [0] * len(T)

        for i, temp in enumerate(T):
            while seen_stack and temp > T[seen_stack[-1]]:
                old_i = seen_stack.pop()
                res[old_i] = i - old_i

            seen_stack.append(i)

        return res


myobj = Solution()
inpt = [73, 74, 75, 71, 69, 72, 76, 73]
print(myobj.dailyTemperatures(inpt))


""" 
[73,0, 74,1, 75,2, 71,3, 69,4, 72,5, 76,6, 73,7]

res = [1, 1, 4, 2, 1, 1, 0, 0]
"""
