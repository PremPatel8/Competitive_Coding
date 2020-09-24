from typing import List
# from collections import defaultdict

"""
Problem Name: Find the Duplicate Number

Problem Section: Array and Strings

Problem Statement:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:
How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1

Constraints:
2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Resources:
"""

""" 53 / 53 test cases passed.
	Status: Accepted
Runtime: 60 ms
Memory Usage: 16.3 MB """

# Solution techniques are Dict solution, Set Solution, Floyd's Tortoise and Hare (Cycle Detection)

# Time complexity : O(n) Space complexity : O(n) Dict solution, Set Solution,
# Time complexity : O(n) Space complexity : O(1) Floyd's Tortoise and Hare (Cycle Detection)


class Solution:
    # Dict sol
    """ def findDuplicate(self, nums: List[int]) -> int:
        numfreq = {}

        for num in nums:
            if num not in numfreq:
                numfreq[num] = 1
            else:
                return num """

    # Set sol
    """ def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num) """

    # Cycle detection sol
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


myobj = Solution()
# inpt = [1, 3, 4, 2, 2]
inpt = [2, 2, 2, 2, 2]
print(myobj.findDuplicate(inpt))
