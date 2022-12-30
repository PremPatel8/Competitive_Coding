from typing import List
"""
Problem Name: Running Sum of 1d Array

Problem URL: https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1

Problem Section: Array

Problem Difficulty: Easy

Problem Statement:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Resources:

"""


class Solution:
    """
    Solution technique: Array traversal creating new result array

    Time & Space Complexity:
    Time - O(n)
    Space - O(n)

    Runtime: 77 ms
    Memory: 14.2 MB
    """
    #     def runningSum(self, nums: List[int]) -> List[int]:
    #         res = [nums[0]]

    #         for idx, no in enumerate(nums[1:],1):
    #             res.append(no+res[idx-1])

    #         return res

    """
    Solution technique: Array traversal reusing the input nums array

    Time & Space Complexity:
    Time - O(n)
    Space - O(1)

    Runtime: 79 ms
    Memory: 14.1 MB
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        for idx, no in enumerate(nums[1:], 1):
            nums[idx] = no + nums[idx-1]

        return nums


myobj = Solution()
inpt = [1,2,3,4]
print(myobj.runningSum(inpt) == [1, 3, 6, 10])


# def test_running_sum():
#     assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
