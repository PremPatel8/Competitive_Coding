from typing import List
"""
Problem Name: Search a 2D Matrix II

Problem Section: Sorting and Searching

Problem Statement:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example:
Input:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
"""

""" 129 / 129 test cases passed.
	Status: Accepted
Runtime: 36 ms
Memory Usage: 18.5 MB """

# Time complexity : O(m+n) Space complexity : O(1)


# Staircase Search solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        height = len(matrix)
        width = len(matrix[0])
        
        # Start at the top right corner
        row = 0
        col = width - 1
        
        while row < height and col >= 0:
            # If current > target → Move LEFT (All elements to its left are smaller, row is sorted)
            if matrix[row][col] > target:
                col -= 1
            # If current < target → Move DOWN, (All elements below it are larger, column is sorted)
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        
        return False


myobj = Solution()
# inpt = [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
# target = 5
# target = 20

inpt = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]
target = 19
print(myobj.searchMatrix(inpt, target))
