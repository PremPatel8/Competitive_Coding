from typing import List

"""
Problem Name: Longest Consecutive Sequence

Problem Section: Array and Strings

Problem Statement:
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Resources:
"""

""" 68 / 68 test cases passed.
	Status: Accepted
Runtime: 60 ms
Memory Usage: 15 MB """

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n) Set Solution


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in nums:
                next_num = num + 1

                while next_num in nums:
                    next_num += 1

                longest_streak = max(longest_streak, next_num - num)

        return longest_streak


myobj = Solution()
inpt = [100, 4, 200, 1, 3, 2]
print(myobj.longestConsecutive(inpt))
