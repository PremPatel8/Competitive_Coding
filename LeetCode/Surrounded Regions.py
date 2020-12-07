from typing import List

"""
Problem Name: Surrounded Regions

Problem URL: https://leetcode.com/problems/surrounded-regions/

Problem Section: DFS, BFS, Union Find

Problem Statement:
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


Resources:

runtime: 

"""

# Solution techniques are

# Time complexity : O() Space complexity : O()
""" 
Iterate through each element in the matrix
if ele is O and it's not been visited added to visited
check if ele is not a boarder element, if not border do DFS search for connected O's and replace them with X
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or len(board) < 3 or len(board[0]) < 3:
            return

        rows = len(board)
        cols = len(board[0])

        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col, region):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            currEle = board[row][col]

            if currEle == "O" and not visited[row][col]:
                region.append((row, col))
                visited[row][col] = True

                dfs(row-1, col, region)
                dfs(row+1, col, region)
                dfs(row, col-1, region)
                dfs(row, col+1, region)

                return region
            else:
                return

        def borderEle(row, col):
            """ element is on the border if the any index of top, bottom, left or right ele is out of bounds of matrix
            top = row-1, y
            bottom = row+1, y
            left = row, col-1
            right = row, col+1
            """

            if row-1 < 0 or row+1 >= rows or col-1 < 0 or col+1 >= cols:
                return True

            return False

        for rw in range(rows):
            for cw in range(cols):
                currEle = board[rw][cw]

                if currEle == "O" and not visited[rw][cw]:
                    # visited[rw][cw] = True

                    if not borderEle(rw, cw):
                        region = dfs(rw, cw, [])
                        print(f"region = {region}")

                        if region:
                            for r, c in region:
                                board[r][c] = "X"

        print(f"board = {board}")


myobj = Solution()
inpt = [['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']]
print(myobj.solve(inpt))
