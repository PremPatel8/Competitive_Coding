from typing import List

"""
Problem Name: Container With Most Water

Problem Section: Array and Strings

Problem URL: https://leetcode.com/problems/container-with-most-water/

Problem Difficulty: Medium

Problem Statement:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49


Resources:

"""

""" 50 / 50 test cases passed.
	Status: Accepted
Runtime: 132 ms
Memory Usage: 15.3 MB """

# Solution techniques are

# Time complexity : O(n) Space complexity : O(1) Two pointer solution


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right-left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


myobj = Solution()
inpt = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# inpt = [1, 1]
print(myobj.maxArea(inpt))
