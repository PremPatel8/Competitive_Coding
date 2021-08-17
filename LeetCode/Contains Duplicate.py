from typing import List

"""
Problem Name: Contains Duplicate

Problem Section: Array

Problem Difficulty: Easy

Problem URL: https://leetcode.com/problems/contains-duplicate/

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
Runtime: 156 ms
Memory Usage: 20.1 MB
 """

# Solution techniques are

# Time complexity : O() Space complexity : O() solution using dict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False
        if len(nums) == 1:
            return False

        freq_count = dict()

        for no in nums:
            if no in freq_count:
                return True
            else:
                freq_count[no] = 1

        return False

    # Optimized Set solution
    """ 20 / 20 test cases passed.
            Status: Accepted
        Runtime: 120 ms
        Memory Usage: 20 MB """

    def containsDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 0 or len(nums) == 1:
            return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False


myobj = Solution()
# inpt = [1, 2, 3, 1]
inpt = [1, 2, 3, 4]
print(myobj.containsDuplicate(inpt))
