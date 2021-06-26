from collections import defaultdict
from typing import List
"""
Problem Name: Single Number

Problem Section: Array

Problem Statement:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

Resources:

"""

""" 16 / 16 test cases passed.
	Status: Accepted
Runtime: 84 ms
Memory Usage: 16.2 MB """

# Solution techniques are

# Time complexity : O(n) Space complexity : O(1) solution using set


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                seen.remove(n)

        return seen.pop()


# Set solution with try catch
# Time - O(n), Space - O(n)
"""
61 / 61 test cases passed.
	Status: Accepted
Runtime: 136 ms
Memory Usage: 16.8 MB
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        singleNum = set()

        for num in nums:
            try:
                singleNum.remove(num)
            except:
                singleNum.add(num)

        return singleNum.pop()


# Hash Table / Dict
# Time - O(n), Space - O(n)
""" 61 / 61 test cases passed.
	Status: Accepted
Runtime: 144 ms
Memory Usage: 16.8 MB """


def singleNumber(self, nums: List[int]) -> int:
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1

    for i in hash_table:
        if hash_table[i] == 1:
            return i


# Bit Manipulation
# Time - O(n), Space - O(1)
""" 61 / 61 test cases passed.
	Status: Accepted
Runtime: 128 ms
Memory Usage: 16.7 MB """


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a


myobj = Solution()
inpt = [4, 1, 2, 1, 2]
print(myobj.singleNumber(inpt))
