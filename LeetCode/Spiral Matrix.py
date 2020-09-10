from typing import List

"""
Problem Name: Spiral Matrix

Problem Section: Array and Strings

Problem Statement:
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Resources:

"""

""" 22 / 22 test cases passed.
	Status: Accepted
Runtime: 28 ms
Memory Usage: 13.8 MB """

# Solution techniques are Simulation, Layer-by-Layer

# Time complexity : O(n) Space complexity : O(1) Layer-by-Layer solution


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1

        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2 + 1):
                ans.append(matrix[r1][c])

            for r in range(r1 + 1, r2 + 1):
                ans.append(matrix[r][c2])

            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    ans.append(matrix[r2][c])
                for r in range(r2, r1, -1):
                    ans.append(matrix[r][c1])

            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1

        return ans


myobj = Solution()
inpt = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(myobj.spiralOrder(inpt))
