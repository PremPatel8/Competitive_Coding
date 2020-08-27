from typing import List

"""
Problem Name: First Bad Version

Problem Section: Sorting and Searching

Problem Statement:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Constraints:
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n

Resources:

"""
""" 22 / 22 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14.1 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() Binary Search solution


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while(left < right):
            mid = left + (right - left) // 2

            if(isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1

        return left


myobj = Solution()
n = 5
myobj.firstBadVersion(n)
