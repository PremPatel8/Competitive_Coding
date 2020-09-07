from typing import List
from collections import defaultdict

"""
Problem Name: Majority Element

Problem Section: Other

Problem Statement:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

Resources:

"""

""" 46 / 46 test cases passed.
	Status: Accepted
Runtime: 176 ms
Memory Usage: 15.4 MB """

# Solution techniques are Frequency Dictionary, Sorting, 

# Time complexity : O(n) Space complexity : O(n) Frequency Dictionary solution


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqDict = defaultdict(int)
        highestFreq = 0
        mostFreq = 0

        for num in nums:
            freqDict[num] += 1
            if freqDict[num] > mostFreq:
                mostFreq = freqDict[num]
                highestFreq = num

        return highestFreq


myobj = Solution()
inpt = [2, 2, 1, 1, 1, 2, 2]
print(myobj.majorityElement(inpt))
