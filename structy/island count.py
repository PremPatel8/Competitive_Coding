""" island count
https://structy.net/problems/island-count

Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.
test_00:

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3
"""

from collections import deque


def island_count(grid):
    rowLen = len(grid)
    colLen = len(grid[0])
    count = 0

    for i in range(rowLen):
        for j in range(colLen):
            if grid[i][j] == 'L':
                bfs(grid, i, j)
                count += 1

    return count


def is_valid(grid, r, c):
    rowLen = len(grid)
    colLen = len(grid[0])

    if r < 0 or c < 0 or r >= rowLen or c >= colLen:
        return False

    return True


def bfs(grid, r, c):
    queue = deque()
    queue.append((r, c))
    grid[r][c] = '#'
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    while queue:
        (currRow, currCol) = queue.popleft()

        for dr, dc in directions:
            if is_valid(grid, currRow+dr, currCol+dc) and grid[currRow+dr][currCol+dc] == 'L':
                queue.append((currRow+dr, currCol+dc))
                grid[currRow+dr][currCol+dc] = 'W'
