from collections import defaultdict, deque
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

    # Alt dfs()
    """ def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        island_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    island_count += 1

        return island_count

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '#'
        
        directions = [(-1,0), (0,1), (1,0), (0,-1)]        
        
        for d1, d2 in directions:
            self.dfs(grid, i+d1, j+d2) """

    # BFS Solution
    """ 
    Time complexity : O(M X N) where M is the number of rows and N is the number of columns.
    Space complexity : O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N)
    """

    def numIslandsBFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def is_valid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True

    def bfs(self, grid, r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'

        while queue:
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'


# Disjoint Set AKA Union Find Solution
class Solution(object):
        def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            if len(grid) == 0:
                return 0
            row = len(grid)
            col = len(grid[0])
            self.count = sum(grid[i][j] == '1' for i in range(row)
                            for j in range(col))
            parent = [i for i in range(row*col)]

            def find(x):
                if parent[x] != x:
                    return find(parent[x])
                return parent[x]

            def union(x, y):
                xroot, yroot = find(x), find(y)
                if xroot == yroot:
                    return
                parent[xroot] = yroot
                self.count -= 1

            for i in range(row):
                for j in range(col):
                    if grid[i][j] == '0':
                        continue
                    index = i*col + j
                    if j < col-1 and grid[i][j+1] == '1':
                        union(index, index+1)
                    if i < row-1 and grid[i+1][j] == '1':
                        union(index, index+col)
            return self.count


myobj = Solution()

# input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

# input = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
#          ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

# input = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]

input = [["1", "0", "1", "1", "1"],
         ["1", "0", "1", "0", "1"],
         ["1", "1", "1", "0", "1"]]

print(myobj.numIslands(input))
# print(myobj.numIslandsBFS(input))
