from typing import List

"""
Problem Name: Shuffle an Array

Problem URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/

Problem Section: Array

Problem Statement:
Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:

    Solution(int[] nums) Initializes the object with the integer array nums.
    int[] reset() Resets the array to its original configuration and returns it.
    int[] shuffle() Returns a random shuffling of the array.


Resources:

runtime: 
10 / 10 test cases passed.
	Status: Accepted
Runtime: 284 ms
Memory Usage: 19.4 MB
"""

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n)


class Solution:

    def __init__(self, nums: List[int]):
        self.original_arr = nums

    def reset(self) -> List[int]:
        return self.original_arr

    def shuffle(self) -> List[int]:
        return random.sample(self.original_arr, len(self.original_arr))


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
