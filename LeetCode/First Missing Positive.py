from typing import List

"""
Problem Name: First Missing Positive

Problem Section: Array and Strings

Problem Statement:
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

Resources:

"""

""" runtime """

# Solution techniques are

# Time complexity : O(n) Space complexity : O(1)
""" 
 1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
2. we can use the array index as the hash to restore the frequency of each number within 
        the range [1,...,l+1] 
after removing all the numbers greater than or equal to n, all the numbers remaining are smaller than n. 
If any number i appears, we add n to nums[i] which makes nums[i]>=n. Therefore, 
if nums[i]<n, it means i never appears in the array and we should return i. """


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        # print(nums)
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        # print(nums)

        for i in range(len(nums)):
            nums[nums[i] % n] += n

        # print(nums)

        for i in range(1, len(nums)):
            if nums[i]//n == 0:
                return i

        return n


myobj = Solution()
inpt = [3, 4, -1, 1]
print(myobj.firstMissingPositive(inpt))
