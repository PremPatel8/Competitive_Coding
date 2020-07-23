from typing import List
import heapq

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

""" 32 / 32 test cases passed.
	Status: Accepted
Runtime: 80 ms
Memory Usage: 14.5 MB """

# O(N lg K) running time + O(K) memory, heap based solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return min(nums)

        minHeap = []

        for num in nums:
            if len(minHeap) == k and num < minHeap[0]:
                continue
            else:
                heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]


myobj = Solution()
# input = [3, 2, 1, 5, 6, 4]
# k = 2
# input = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
input = [7, 6, 5, 4, 3, 2, 1]
k = 2
print(myobj.findKthLargest(input, k))
