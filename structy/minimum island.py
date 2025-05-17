""" minimum island
https://structy.net/problems/minimum-island

Write a function, minimum_island, that takes in a grid containing Ws and Ls.
W represents water and L represents land.
The function should return the size of the smallest island.
An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.
test_00:

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2
"""

def minimum_island(grid):
    min_size = float('inf')
    rowLen = len(grid)
    colLen = len(grid[0])

    for r in range(rowLen):
        for c in range(colLen):
            if grid[r][c] == 'L':
                size = dfs(grid, r, c)
                if 0 < size < min_size:
                    min_size = size

    return min_size


def is_valid(grid, r, c):
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 'L':
        return True
    return False


def dfs(grid, r, c):
    if not is_valid(grid, r, c):
        return 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    grid[r][c] = '#'
    island_size = 1

    for dr, dc in directions:
        island_size += dfs(grid, r+dr, c+dc)

    return island_size
