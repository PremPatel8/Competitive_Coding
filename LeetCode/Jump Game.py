from typing import List
from collections import defaultdict

"""
Problem Name: Jump Game

Problem Section: Dynamic Programming

Problem Statement:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.


Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
"""

""" 75 / 75 test cases passed.
	Status: Accepted
Runtime: 100 ms
Memory Usage: 15.7 MB """

# Time complexity : O() Space complexity : O(1) Greedy Solution
# Time Limit Exceeded


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        if len(nums) == 1:
            return True

        dist = i = 0

        while(i <= dist):
            dist = max(dist, i+nums[i])

            if(dist >= len(nums)-1):
                return True

            i += 1

        return False


myobj = Solution()
inpt = [2, 3, 1, 1, 4]
# inpt = [3, 2, 1, 0, 4]
# inpt = [1, 0, 1, 0]
# inpt = [2, 0]
print(myobj.canJump(inpt))
