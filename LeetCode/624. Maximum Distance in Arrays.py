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
# ## 624. Maximum Distance in Arrays
# - Description:
#   <blockquote>
#     [624. Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays/) You are given `m` `arrays`, where each array is sorted in **ascending order**.
#      
#     You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers `a` and `b` to be their absolute difference `|a - b|`.
#      
#     Return  *the maximum distance* .
#      
#     **Example 1:**
#     **Input:** arrays = `[1, 2,3],[4,5],[1,2,3]`
#     **Output:** 4
#     **Explanation:** One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
#      
#     **Example 2:**
#     **Input:** arrays = `[1], [1]`
#     **Output:** 0
#      
#     **Constraints:**
#      
#     - `m == arrays.length`
#     - `2 <= m <= 105`
#     - `1 <= arrays[i].length <= 500`
#     - `-104<= arrays[i][j] <= 104`
#     - `arrays[i]` is sorted in **ascending order**.
#     - There will be at most `105` integers in all the arrays.
#   </blockquote>
#
# - URL: [Problem_URL](https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=company&envId=yahoo&favoriteSlug=yahoo-all)
#
# - Topics: Greedy
#
# - Difficulty: Easy / Medium
#
# - Resources: example_resource_URL

# %% [markdown]
# ### Solution 1, Brute Force TLE
# Solution description
# - Time Complexity: O(N^2)
#   - We consider only max and min values directly for every array currenty considered. Here, n refers to the number of arrays in arrays.
# - Space Complexity: O(1)

# %%
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0

        for i in range(0, len(arrays)):
            for j in range(i+1, len(arrays)):
                arr1 = arrays[i]
                arr2 = arrays[j]
                
                result = max(result, abs(arr2[-1]-arr1[0]))
                result = max(result, abs(arr1[-1]-arr2[0]))
        
        return result


# %% [markdown]
# ### Solution 2, Greedy Single Scan
# - Time Complexity: O(N)
# - Space Complexity: O(1)

# %%
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_no = arrays[0][0]
        max_no = arrays[0][-1]

        res = 0

        for i in range(1, len(arrays)):
            curr_max_dist = max(abs(arrays[i][-1]-min_no), abs(max_no-arrays[i][0]))
            res = max(res, curr_max_dist)

            min_no = min(arrays[i][0], min_no)
            max_no = max(arrays[i][-1], max_no)
        
        return res
