from typing import List

"""
Problem Name: Pascal's Triangle

Problem Section: Others / Bit Manipulation

Problem Statement:
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
 
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Resources:

"""

""" 15 / 15 test cases passed.
	Status: Accepted
Runtime: 24 ms
Memory Usage: 13.9 MB """

# Solution techniques are
# Time complexity : O(numRows**2) Space complexity : O(numRows**2) DP Soluion


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]

            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle


myobj = Solution()
inpt = 5
print(myobj.generate(inpt))
