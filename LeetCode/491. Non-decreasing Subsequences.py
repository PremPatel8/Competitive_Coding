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
# ## 491. Non-decreasing Subsequences
# - Description:
#   <blockquote>
#         [491. Non-decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences/) Given an integer array `nums`, return  *all the different possible non-decreasing subsequences of the given array with at least two elements* . You may return the answer in **any order**.
#      
#     **Example 1:**
#     **Input:** nums = [4,6,7,7]
#     **Output:** `[4, 6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]`
#      
#     **Example 2:**
#     **Input:** nums = [4,4,3,2,1]
#     **Output:** `[4, 4]`
#      
#     **Constraints:**
#      
#     - `1 <= nums.length <= 15`
#     - `-100 <= nums[i] <= 100`
#   </blockquote>
#
# - URL: [Problem_URL](https://leetcode.com/problems/non-decreasing-subsequences/description/?envType=company&envId=yahoo&favoriteSlug=yahoo-all)
#
# - Topics: Backtracking
#
# - Difficulty: Medium
#
# - Resources: example_resource_URL

# %% [markdown]
# ### Solution 1, Backtracking, Most Common Solution
#
#
# - Time Complexity: O(2^N * N)
#   - In the worst case (e.g., `nums` strictly increasing), **every subsequence** is non-decreasing.
#   - Number of subsequences of an array of length `n` is `2^n` (each element either taken or not).
#   - For each subsequence we:
#     - Spend up to `O(n)` to copy `path` into `res`.
#     - Do some extra `O(1)` / `O(log n)` work in the `used` set per level, which doesn’t change the exponential nature.
# - Space Complexity: O(2^N * N)
#   - `res` stores up to `2^n` subsequences.
#   - Each subsequence has length up to `n`.
#   - So storing all of them costs `2^n * n` space.
#   - The `n` here = **max length of each stored subsequence**.
#
#   **Auxiliary space `O(n^2)`:**
#   - Call stack: `O(n)`
#   - `path`: `O(n)`
#   - `used` sets: `O(n^2)`
#   - Total auxiliary: `O(n^2)`
#
#   Since `2^n` grows much faster than `n^2`, the auxiliary space `O(n^2)` is completely **dominated** by the output space `O(2^n · n)`.

# %%
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(idx):
            if len(path) > 1:
                res.append(path[:])
            
            # used to skip numbers that have already been used for a subsequence (aka duplicates) at the current recursion depth
            used = set()

            for i in range(idx, len(nums)):
                # Ignore any numbers that are not greater than or equal to the last element of the current path (aka break the non-decreasing subsequences)
                if path and nums[i] < path[-1] or nums[i] in used:
                    continue
                
                used.add(nums[i])
                
                path.append(nums[i])
                
                backtrack(i+1)
                
                path.pop()
        
        backtrack(0)

        return res
