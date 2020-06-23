from typing import List

""" Runtime: 128 ms
Memory Usage: 14.4 MB """
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroLocations = []
        indexSeen = dict()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroLocations.append([i, j])

        for r, c in zeroLocations:
            row = "R"+str(r)
            col = "C"+str(c)

            if row not in indexSeen:
                indexSeen[row] = None
                matrix[r] = [0]*len(matrix[0])

            if col not in indexSeen:
                indexSeen[col] = None

                for r in range(len(matrix)):
                    matrix[r][c] = 0
        
        # print(matrix)
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))


myClassObj = Solution()

# inpt = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
inpt = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

myClassObj.setZeroes(inpt)
