from typing import List
import heapq

"""
Problem Name: 378. Kth Smallest Element in a Sorted Matrix

Problem Section: Array, Matrix, Heap, Binary Search

Problem Statement:
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

Resources:
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85193/Binary-Search-Heap-and-Sorting-comparison-with-concise-code-and-1-liners-Python-72-ms
"""

""" 85 / 85 test cases passed.
	Status: Accepted
Runtime: 204 ms
Memory Usage: 20 MB """

# Solution techniques are Binary Search, Heap

# Time complexity : O(k * log n) Space complexity : O(n)
# The time complexity is O(k * log n), so the worst-case and average-case time complexity is O(n^2 * log n). Space complexity is O(n).


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0

        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))

        return ret


myobj = Solution()
matrix = [[1,  5,  9],
          [10, 11, 13],
          [12, 13, 15]]
k = 8
print(myobj.kthSmallest(matrix, k))
