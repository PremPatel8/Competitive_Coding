from typing import List
import collections

"""
Problem Name: 532. K-diff Pairs in an Array

Problem URL: https://leetcode.com/problems/k-diff-pairs-in-an-array/

Problem Section: dict, array, two pointer

Problem Statement:
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

    0 <= i, j < nums.length
    i != j
    |nums[i] - nums[j]| == k

Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.


Resources:
https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/100135/JavaPython-Easy-Understood-Solution

runtime: 
59 / 59 test cases passed.
	Status: Accepted
Runtime: 72 ms
Memory Usage: 15.6 MB
"""

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n)


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        num_freq = collections.Counter(nums)
        for no in num_freq:
            if (k > 0 and no + k in num_freq) or (k == 0 and num_freq[no] > 1):
                res += 1
        return res


myobj = Solution()
nums = [3, 1, 4, 1, 5]
k = 2
print(myobj.findPairs(nums, k))
