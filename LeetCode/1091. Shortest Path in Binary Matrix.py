# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
# ---

# %% [markdown]
# ## 1091. Shortest Path in Binary Matrix
# - Description:
#   <blockquote>
#     [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) Given an `n x n` binary matrix `grid`, return  *the length of the shortest **clear path** in the matrix* . If there is no clear path, return `-1`.
#      
#     A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:
#      
#     - All the visited cells of the path are `0`.
#     - All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).
#      
#     The **length of a clear path** is the number of visited cells of this path.
#      
#     **Example 1:**
#     ![Image](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)
#      
#     **Input:** grid = `[0, 1],[1,0]`
#     **Output:** 2
#      
#     **Example 2:**
#     ![Image](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)
#      
#     **Input:** grid = `[0, 0,0],[1,1,0],[1,1,0]`
#     **Output:** 4
#      
#     **Example 3:**
#     **Input:** grid = `[1, 0,0],[1,1,0],[1,1,0]`
#     **Output:** -1
#      
#     **Constraints:**
#      
#     - `n == grid.length`
#     - `n == grid[i].length`
#     - `1 <= n <= 100`
#     - `grid[i][j] is 0 or 1`
#   </blockquote>
#
# - URL: [Problem_URL](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/?envType=company&envId=yahoo&favoriteSlug=yahoo-all)
#
# - Topics: Problem_topic
#
# - Difficulty: Medium
#
# - Resources: example_resource_URL

# %% [markdown]
# ### Solution 1, Most Efficient BFS overwriting the grid cells for both visited and distance
# Let N be the number of cells in the grid.
#
# - Time Complexity: O(N)
#   - Each cell is enqueued at most once — when first discovered
#   - Per cell, we check 8 directions → O(1) work per cell
# - Space Complexity: O(N)
#   - In the worst case (all cells are 0), all cells could be enqueued 

# %%
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        if grid[0][0] != 0 or grid[row_len-1][col_len-1] != 0:
            return -1

        directions = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1  # mark visited by putting the distance count in the cell

        while queue:
            c_row, c_col = queue.popleft()
            distance = grid[c_row][c_col]

            if (c_row, c_col) == (row_len-1, col_len-1):
                return distance

            for dr, dc in directions:
                nr, nc = c_row+dr, c_col+dc

                if 0 <= nr <= row_len-1 and 0 <= nc <= col_len-1 and grid[nr][nc] == 0:
                    grid[nr][nc] = distance + 1
                    queue.append((nr, nc))

        return -1


# %% [markdown]
# ### Solution 1, My BFS sol, imperfect, without overwriting cells, using visited matrix and putting distance on the queue
# Solution description
# - Time Complexity: O(N)
# - Space Complexity: O(N)

# %%
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        res = -1
        row_len = len(grid)
        col_len = len(grid[0])

        if grid[0][0] != 0 or grid[row_len-1][col_len-1] != 0:
            return res

        directions = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

        queue = deque()
        queue.append((0,0,1))
        # Since BFS processes level by level, when you first enqueue a neighbor it can never be reached by a shorter path later, 
        # so a separate visited data structure is unnecessary, we can just modify the grid value for visited cells directly
        visited = [[0 for _ in range(col_len)] for _ in range(row_len)]
        visited[0][0] = 1

        while queue:
            cr, cc, path_len = queue.popleft()

            # Since BFS processes nodes level by level, the first time you dequeue the destination is guaranteed to be the shortest path.
            # There's no need to do this
            if cr == row_len-1 and cc == col_len-1:
                res = min(res, path_len) if res != -1 else path_len

            for dr, dc in directions:
                nr, nc = cr+dr, cc+dc

                if 0 <= nr <= row_len-1 and 0 <= nc <= col_len-1 and visited[nr][nc] == 0 and grid[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, path_len+1))

        return res


# %% [markdown]
# ### BFS, Overwriting Input

# %%
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1
        
        # Carry out the BFS.
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            
            if (row, col) == (max_row, max_col):
                return distance
            
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                grid[neighbour_row][neighbour_col] = distance + 1
                queue.append((neighbour_row, neighbour_col))
        
        # There was no path.
        return -1


# %% [markdown]
# ### BFS, Without Overwriting Input

# %%
# Distances on queue | Similar to my BFS sol

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0, 1)])
        
        # using a visited set to avoid overiting the input grid
        visited = {(0, 0)}
        
        # Do the BFS.
        while queue:
            row, col, distance = queue.popleft()
            if (row, col) == (max_row, max_col):
                return distance
            
            for neighbour in get_neighbours(row, col):
                if neighbour in visited:
                    continue
            
                visited.add(neighbour)
                # Note that the * splits neighbour into its values.
                queue.append((*neighbour, distance + 1))
                
        # There was no path.
        return -1


# %%
# Claud sol

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        directions = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
        queue = deque([(0, 0, 1)])  # (row, col, path_len)
        grid[0][0] = 1  # mark visited
        
        while queue:
            row, col, path_len = queue.popleft()
            
            if row == n-1 and col == n-1:
                return path_len
            
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # mark visited immediately
                    queue.append((nr, nc, path_len+1))
        
        return -1


# %%
# Starting a new collection for each distance | unnecessarily complicates normal BFS IMO

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        current_layer = [(0, 0)]
        next_layer = []
        visited = {(0, 0)}
        current_distance = 1
        
        while current_layer:
            
            # Process the current layer.
            for row, col in current_layer:
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    next_layer.append(neighbour)
            
            # Set up for processing the next layer.
            current_distance += 1
            current_layer = next_layer
            next_layer = []
                
        # There was no path.
        return -1


# %%
# Keeping track of how many cells at each distance are on the queue

class Solution:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        current_distance = 1
        
        # Do the BFS.
        while queue:
            # Process all nodes at current_distance from the top-left cell.
            nodes_of_current_distance = len(queue)
            for _ in range(nodes_of_current_distance):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)
            # We'll now be processing all nodes at current_distance + 1
            current_distance += 1
                    
        # There was no path.
        return -1 
