from typing import List


"""
Problem Name: 42. Trapping Rain Water

Problem Section: Array, Two Pointers, Stack

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Resources:

"""
""" 315 / 315 test cases passed.
	Status: Accepted
Runtime: 48 ms
Memory Usage: 14.7 MB """

# Solution techniques are Dynamic Programming (2 for loops to create left max and right max arrays), Using stacks, Using 2 pointers
# Time complexity : O(n) Space complexity : O(1) Optimized solution using 2 pointers
""" 
Complexity analysis
Time complexity: O(n) Single iteration of O(n)
Space complexity: O(1) extra space. Only constant space required for left, right, left_max and right_max
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 0:
            return 0

        ans = left_max = right_max = 0

        left_ptr = 0
        right_ptr = len(height)-1

        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                if height[left_ptr] >= left_max:
                    left_max = height[left_ptr]
                else:
                    ans += left_max - height[left_ptr]
                left_ptr += 1
            else:
                if height[right_ptr] >= right_max:
                    right_max = height[right_ptr]
                else:
                    ans += right_max-height[right_ptr]
                right_ptr -= 1

        return ans


myobj = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(myobj.trap(height))
# Output: 6
