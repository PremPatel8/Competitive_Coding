from typing import List

"""
Problem Name: 448. Find All Numbers Disappeared in an Array

Problem URL: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Problem Section: Array

Problem Statement:
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


Resources:
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92955/Python-4-lines-with-short-explanation

runtime: 
34 / 34 test cases passed.
	Status: Accepted
Runtime: 364 ms
Memory Usage: 21.9 MB

"""

# Solution techniques are

# Time complexity : O(n) Space complexity : O(1) output list not counted


class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     for num in nums:
    #         index = abs(num) - 1
    #         nums[index] = -abs(nums[index])

    #     return [i + 1 for i, num in enumerate(nums) if num > 0]

    # Alt syntax
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i, num in enumerate(nums) if num > 0]


myobj = Solution()
inpt = [4, 3, 2, 7, 8, 2, 3, 1]

print(myobj.findDisappearedNumbers(inpt))
