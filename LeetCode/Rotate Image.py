from typing import List

"""
Problem Name: Rotate Image

Problem Section: Array

Problem Statement:
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]


Resources:
"""
""" 21 / 21 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 13.6 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O()


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        # print(matrix)
        # matrix[:] = map(list, zip(*matrix))

        size = len(matrix)

        for i in range(size):
            for j in range(i+1, size):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        return matrix


    # My Alt sol
    """ 21 / 21 test cases passed.
          Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14.4 MB """
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            row.reverse()

        size = len(matrix)

        for r in range(size-1):
            for c in range(size-1-r):
                # print(f"r={r}, c={c}")
                matrix[r][c], matrix[size-1-c][size-1-r] = matrix[size-1-c][size-1-r], matrix[r][c]

        return matrix


myobj = Solution()
inpt = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

""" Opt = [7, 4, 1],
          [8, 5, 2],
          [9, 6, 3] """

print(myobj.rotate(inpt))
