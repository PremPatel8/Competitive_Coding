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
Runtime: 30 ms
Memory Usage: 13.9 MB """

# Solution techniques are
# Time complexity : O(numRows**2) Space complexity : O(numRows**2) Offset sum trick
""" 
 Any row can be constructed using the offset sum of the previous row. Example:

    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1
 """


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        res = [[1]]
        for _ in range(1, numRows):
            map_ = map(lambda x, y: x+y, [0] + res[-1], res[-1] + [0])

            res.append(list(map_))

        return res


myobj = Solution()
inpt = 5
print(myobj.generate(inpt))
