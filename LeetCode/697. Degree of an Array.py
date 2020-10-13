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
Runtime: 232 ms
Memory Usage: 15 MB
"""

# Solution techniques are iterate through array multiple times to generate left, right and freq count dicts, to get max freq count and again to get min subarray len

# Time complexity : O(n) Space complexity : O(n)

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
        left_idx, freq_count, res, degree = {}, {}, 0, 0

        for i, num in enumerate(nums):
            if num not in left_idx:
                left_idx[num] = i
            # left_idx.setdefault(num, i)

            # freq_count[num] = freq_count.get(num, 0) + 1
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1

            if freq_count[num] > degree:
                degree = freq_count[num]
                res = i - left_idx[num] + 1
            elif freq_count[num] == degree:
                res = min(res, i - left_idx[num] + 1)

        return res


myobj = Solution()
# inpt = [1, 2, 2, 3, 1, 4, 2]
# inpt = [1, 1, 2, 2, 2, 1]
# inpt = [2, 1, 1, 2, 1, 3, 3, 3, 1, 3, 1, 3, 2]
inpt = [2, 1]

print(f"{myobj.findShortestSubArray(inpt)} == 1 : {myobj.findShortestSubArray(inpt) == 1}")
