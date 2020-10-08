from typing import List
import bisect

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
"""

""" 85 / 85 test cases passed.
	Status: Accepted
Runtime: 152 ms
Memory Usage: 19.9 MB """

# Solution techniques are Binary Search, Heap

# Time complexity : O(n log n) Space complexity : O(1)
# The time complexity is O(n * log(n) * log(N)), where N is the search space that ranges from the smallest element to the biggest element.
# You can argue that int implies N = 2^32, so log(N) is constant. In a way, this is an O(n * log(n)) solution.


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo = matrix[0][0]
        hi = matrix[-1][-1]

        while lo < hi:
            mid = (lo+hi)//2
            no_ele_less_than_mid = 0

            for row in matrix:
                no_ele_less_than_mid += bisect.bisect_right(row, mid)

            if no_ele_less_than_mid < k:
                lo = mid+1
            else:
                hi = mid
        return lo


myobj = Solution()
matrix = [[1,  5,  9], [10, 11, 13], [12, 13, 15]]
k = 8
print(myobj.kthSmallest(matrix, k))
