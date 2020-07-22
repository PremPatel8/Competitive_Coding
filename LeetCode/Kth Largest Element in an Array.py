from typing import List

"""
Problem Name: Kth Largest Element in an Array

Problem Section: Sorting and Searching

Problem Statement:
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

""" 21 / 21 test cases passed.
	Status: Accepted
Runtime: 124 ms
Memory Usage: 18.3 MB """

# O(nlogn) naive solution using sorting
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


myobj = Solution()
# input = [3, 2, 1, 5, 6, 4]
# k = 2
input = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(myobj.findKthLargest(input, k))
