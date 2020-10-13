from typing import List
from collections import defaultdict

"""
Problem Name: 1010. Pairs of Songs With Total Durations Divisible by 60

Problem URL: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

Problem Section: Array

Problem Statement:
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60


Resources:
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/642553/Python-O(n)-with-simple-math-explanation

runtime: 
34 / 34 test cases passed.
	Status: Accepted
Runtime: 232 ms
Memory Usage: 18 MB
"""

# Solution techniques are

# Time complexity : O() Space complexity : O()

""" 
I = unsorted array of numbers, duplicates allowed
O = no. of pairs whose total time is divisible by 60
C = 1 <= time.length <= 60000, 1 <= time[i] <= 500

[30,20,150,100,40]
30+150 = 180/60 = 3
20+100 = 120/60 = 2
20+40 = 60/60 = 1

60 = 6 * 10
2 * 2 * 3 * 5

30+150 / 60 = 3
(30/60 + 150/60)/60 = 3

1/2 + 15/6 = 3

"""


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        ans = 0

        for t in time:
            t_mod = t % 60

            find = 0 if t_mod == 0 else 60 - t_mod
            ans += count[find]
            count[t_mod] += 1

        return ans


myobj = Solution()
inpt = [30, 20, 150, 100, 40]
print(myobj.numPairsDivisibleBy60(inpt))
