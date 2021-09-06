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

Resources:
https://leetcode.com/problems/number-of-islands/discuss/56519/Union-Find-in-Python
"""

"""
DFS technique used to traverse 2D List / Matrix and mark all adjacent islands ("1") as '#'
each time control comes back from DFS function increment island counter by 1 as all the reachable islands have been marked # by that point
"""


class Solution:
    """ def numIslands(self, grid: List[List[str]]) -> int:
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
        self.dfs(grid, i, j-1) """

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

    """ def numIslandsBFS(self, grid):
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
                    grid[nr][nc] = '0' """

    # Disjoint Set AKA Union Find Solution
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0

        rowLen = len(grid)
        colLen = len(grid[0])
        self.count = 0

        # initialize a parent array where each element in the 0 indexed matrix
        # is it's own parent
        parent = [i for i in range(rowLen*colLen)]
        rank = [0] * rowLen*colLen

        # initialize minimum island count to the count of all the individual lands in the matrix
        # cause if none of the lands are conncted to each other then we have L islands count total (max count of islands)
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == '1':
                    self.count += 1

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            xroot = find(x)
            yroot = find(y)

            if xroot == yroot:
                return
            if rank[xroot] < rank[yroot]:
                xroot, yroot = yroot, xroot

            parent[yroot] = xroot
            rank[xroot] = max(rank[xroot], rank[yroot]+1)

            # If we are joining islands then we are reducing the count of individual islands by 1
            self.count -= 1

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == '0':
                    continue
                index = i*colLen + j
                if j < colLen-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < rowLen-1 and grid[i+1][j] == '1':
                    union(index, index+colLen)
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
