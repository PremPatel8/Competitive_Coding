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
Runtime: 340 ms
Memory Usage: 19.6 MB
"""

# Solution techniques are Fisher-Yates Algorithm
""" The Fisher-Yates algorithm is remarkably similar to the brute force solution. 
On each iteration of the algorithm, we generate a random integer between the current index and the last index of the array. 
Then, we swap the elements at the current index and the chosen index - this simulates drawing (and removing) the element from the hat, 
as the next range from which we select a random index will not include the most recently processed one. 
One small, yet important detail is that it is possible to swap an element with itself - otherwise, 
some array permutations would be more likely than others. """

# Time complexity : O(n) Space complexity : O(n)


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original_arr = list(nums)

    def reset(self) -> List[int]:
        self.array = self.original_arr
        self.original_arr = list(self.original_arr)
        return self.array

        return self.original_arr

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]

        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
