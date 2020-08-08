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

# Time complexity : O() Space complexity : O() solution using


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                seen.remove(n)

        return seen.pop()


myobj = Solution()
inpt = [4, 1, 2, 1, 2]
print(myobj.singleNumber(inpt))


""" 
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i
 """