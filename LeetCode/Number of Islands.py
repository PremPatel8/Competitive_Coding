from collections import defaultdict
from typing import List

"""
Number of Islands: 
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is 
formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. 
 
Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3 
"""

""" 
DFS technique used to traverse 2D List / Matrix and mark all adjacent islands ("1") as '#'
each time control comes back from DFS function increment island counter by 1 as all the reachable islands have been marked # by that point
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        island_count = 0

        for r, row in enumerate(grid):
            for c, land in enumerate(row):
                if land == "1":
                    self.dfs(grid, r, c)
                    island_count += 1

        return island_count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


myobj = Solution()

# input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

# input = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
#          ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

# input = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]

input = [["1", "0", "1", "1", "1"], [
    "1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]]

print(myobj.numIslands(input))
