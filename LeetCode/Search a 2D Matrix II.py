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
Memory Usage: 18.4 MB """

# Time complexity : O() Space complexity : O() My Solution


class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row_count = []
        column_count = []

        for itr, row in enumerate(matrix):
            if row[0] == target or row[-1] == target:
                return True
            elif row[0] < target < row[-1]:
                row_count.append(itr)

        if len(row_count) == 0:
            return False

        rows = len(matrix)-1
        columns = len(matrix[0])

        for col in range(columns):
            if matrix[0][col] == target or matrix[rows][col] == target:
                return True
            elif matrix[0][col] < target < matrix[rows][col]:
                column_count.append(col)

        if len(column_count) == 0:
            return False

        for ro in row_count:
            if target in matrix[ro][column_count[0]:column_count[-1]+1]:
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
