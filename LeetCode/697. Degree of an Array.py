from typing import List
from collections import defaultdict

"""
Problem Name: 697. Degree of an Array

Problem URL: https://leetcode.com/problems/degree-of-an-array/

Problem Section: Array

Problem Statement:
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.


Resources:

runtime: 
89 / 89 test cases passed.
	Status: Accepted
Runtime: 252 ms
Memory Usage: 15.3 MB
"""

# Solution techniques are iterate through array and update dict with [freq, Last Seen Index, Subarray len so far]

# Time complexity : O(n) Space complexity : O(1)

"""
1, 2, 2, 3, 1, 4, 2

0 1 2 3 4 5 6 7 8 9 ...
  1 2

1 - [0,]
2 - [1,1]
3 - [3]

"""


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        freq_degree = defaultdict(list)
        res = len(nums)
        max_freq = 0

        for i, num in enumerate(nums):
            if not freq_degree[num]:
                freq_degree[num].append(1)
                freq_degree[num].append(i)
                freq_degree[num].append(1)
            else:
                freq_degree[num][0] += 1
                temp = freq_degree[num][1]
                freq_degree[num][1] = i
                freq_degree[num][2] += i-temp

                if freq_degree[num][0] >= max_freq:
                    if freq_degree[num][0] > max_freq:
                        res = freq_degree[num][2]
                    else:
                        res = min(res, freq_degree[num][2])

                    max_freq = freq_degree[num][0]

        return res if max_freq != 0 else 1


myobj = Solution()
# inpt = [1, 2, 2, 3, 1, 4, 2]
# inpt = [1, 1, 2, 2, 2, 1]
# inpt = [2, 1, 1, 2, 1, 3, 3, 3, 1, 3, 1, 3, 2]
inpt = [2, 1]

print(f"{myobj.findShortestSubArray(inpt)} == 1 : {myobj.findShortestSubArray(inpt) == 1}")
