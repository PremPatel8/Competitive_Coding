from typing import List

"""
Problem Name: Rotate Array

Problem Section: Array

Problem Statement:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Constraints:
1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0


Resources:

"""

""" 35 / 35 test cases passed.
	Status: Accepted
Runtime: 64 ms
Memory Usage: 15.3 MB """

# Solution techniques are Using Extra Array and Using Cyclic Replacements

# Time complexity : O(n) Space complexity : O(n) Using Extra Array


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a
        return nums


myobj = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(myobj.rotate(nums, k))
