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
# ## 1030. Matrix Cells in Distance Order
# - Description:
#   <blockquote>
#         [1030. Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/) You are given four integers `row`, `cols`, `rCenter`, and `cCenter`. There is a `rows x cols` matrix and you are on the cell with the coordinates `(rCenter, cCenter)`.
#          
#         Return  *the coordinates of all cells in the matrix, sorted by their **distance** from* `(rCenter, cCenter)` *from the smallest distance to the largest distance* . You may return the answer in **any order** that satisfies this condition.
#          
#         The **distance** between two cells `(r1, c1)` and `(r2, c2)` is `|r1- r2| + |c1- c2|`.
#          
#         **Example 1:**
#         **Input:** rows = 1, cols = 2, rCenter = 0, cCenter = 0
#         **Output:** `[0, 0],[0,1]`
#         **Explanation:** The distances from (0, 0) to other cells are: [0,1]
#          
#         **Example 2:**
#         **Input:** rows = 2, cols = 2, rCenter = 0, cCenter = 1
#         **Output:** `[0, 1],[0,0],[1,1],[1,0]`
#         **Explanation:** The distances from (0, 1) to other cells are: [0,1,1,2]
#         The answer `[0, 1],[1,1],[0,0],[1,0]` would also be accepted as correct.
#          
#         **Example 3:**
#         **Input:** rows = 2, cols = 3, rCenter = 1, cCenter = 2
#         **Output:** `[1, 2],[0,2],[1,1],[0,1],[1,0],[0,0]`
#         **Explanation:** The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
#         There are other answers that would also be accepted as correct, such as `[1, 2],[1,1],[0,2],[1,0],[0,1],[0,0]`.
#          
#         **Constraints:**
#          
#         - `1 <= rows, cols <= 100`
#         - `0 <= rCenter < rows`
#         - `0 <= cCenter < cols`
#   </blockquote>
#
# - URL: [Problem_URL](https://leetcode.com/problems/matrix-cells-in-distance-order/?envType=company&envId=yahoo&favoriteSlug=yahoo-all)
#
# - Topics: BFS, Bucket Sort,Sort with custom key
#
# - Difficulty: Easy
#
# - Resources: example_resource_URL

# %% [markdown]
# ### Solution 1, Bucket/Counting Sort by Distance Approach, most efficient
#
# #### Maximum Manhattan Distance in a Grid
#
# The Manhattan distance formula is: **|r₁ - r₂| + |c₁ - c₂|**
#
# In a `rows × cols` matrix:
# - Row indices range from **0 to rows-1**
# - Column indices range from **0 to cols-1**
#
# The **maximum possible distance** occurs between two opposite corners of the matrix:
#
# **Example**: From top-left corner (0, 0) to bottom-right corner (rows-1, cols-1)
#
# ```
# Distance = |0 - (rows-1)| + |0 - (cols-1)|
#          = (rows-1) + (cols-1)
#          = rows + cols - 2
# ```
#
# #### Why this matters for the problem:
#
# Since the center point (rCenter, cCenter) is somewhere inside the matrix, the farthest any cell can be from it is still bounded by this maximum corner-to-corner distance.
#
# **Practical implication**: 
# - If `rows = 100` and `cols = 100` (maximum constraints)
# - Max distance = 100 + 100 - 2 = **198**
# - This small, predictable range makes bucket/counting sort very efficient!
#
# This bounded distance range is what makes the counting sort approach O(n) instead of O(n log n) - we can create exactly `rows + cols - 1` buckets (distances 0 to rows+cols-2) and distribute cells into them in a single pass.
#
# - Time Complexity: O(N)
#   - O(N + D) where D is max distance (rows + cols - 2).
#   - Here D ≤ 198, so effectively O(N)
#   - One pass to compute distance and push into buckets.
#   - One pass to concatenate buckets.
# - Space Complexity: O(N)

# %%
from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # Maximum possible Manhattan distance in the grid
        max_dist = rows + cols - 2

        # Buckets where index = distance, value = list of cells at that distance
        buckets = [[] for _ in range(max_dist + 1)]

        # Fill the buckets
        for r in range(rows):
            for c in range(cols):
                d = abs(r - rCenter) + abs(c - cCenter)
                buckets[d].append([r, c])

        # Concatenate buckets in order of distance
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result


# %% [markdown]
# ### Solution 2, BFS
# Solution description
# - Time Complexity: O(N)
#   - Each cell is enqueued/dequeued at most once, and for each we check 4 neighbors → O(4N) = O(N).
# - Space Complexity: O(N)
# - O(N) for visited + queue in the worst case.

# %%
from collections import deque
from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * cols for _ in range(rows)]
        queue = deque()
        result = []

        queue.append((rCenter, cCenter))
        visited[rCenter][cCenter] = True

        while queue:
            r, c = queue.popleft()
            result.append([r, c])

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return result


# %% [markdown]
# ### Solution 3, Sort with key approach
# Solution description
# - Time Complexity: O(N log N)
#   - due to sorting all cells by distance
# - Space Complexity: O(N)
#   - typically O(N) in Python’s Timsort in the worst case.

# %%
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells = []

        # Generate all cells
        for r in range(rows):
            for c in range(cols):
                cells.append([r, c])

        # Sort by Manhattan distance to (rCenter, cCenter)
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

        return cells
