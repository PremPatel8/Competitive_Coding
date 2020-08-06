from typing import List

"""
Problem Name: Contains Duplicate

Problem Section: Array

Problem Statement:
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example:
Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false

Resources:
"""

""" 
18 / 18 test cases passed.
	Status: Accepted
Runtime: 128 ms
Memory Usage: 19.2 MB
 """

# Solution techniques are

# Time complexity : O() Space complexity : O() Naive solution using Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (len(nums) == len(set(nums)))


myobj = Solution()
inpt = [1, 2, 3, 1]
print(myobj.containsDuplicate(inpt))
