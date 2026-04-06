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
# ## 312. Burst Balloons
# - Description:
#   <blockquote>
#   [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/) You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.
#  
# If you burst the `ith` balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.
#  
# Return  *the maximum coins you can collect by bursting the balloons wisely* .
#  
# **Example 1:**
# **Input:** nums = [3,1,5,8]
# **Output:** 167
# **Explanation:**
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#  
# **Example 2:**
# **Input:** nums = [1,5]
# **Output:** 10
#  
# **Constraints:**
#  
# - `n == nums.length`
# - `1 <= n <= 300`
# - `0 <= nums[i] <= 100`
#   </blockquote>
#
# - URL: [Problem_URL](https://leetcode.com/problems/burst-balloons/description/)
#
# - Topics: Recursion+Memo, DP
#
# - Difficulty: Hard
#
# - Resources: example_resource_URL

# %% [markdown]
# ### Solution 1, Naive Recursion + Memoization
# Solution description
# - Time Complexity: O(N)
# - Space Complexity: O(N)

# %%
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        pass
        # // return maximum coins obtainable if we burst all balloons in `nums`.
        # function dp(nums, memo_dict) {
        #     // check if have we seen this dp_state
        #     if dp_state in memo_dict
        #         return memo_dict[dp_state]

        #     // base case
        #     if nums is empty
        #         return 0
            
        #     max_coins = 0
        #     for i in 1 ... nums.length - 2:
        #         // burst nums[i]
        #         gain = nums[i - 1] * nums[i] * nums[i + 1]
        #         // burst the remaining balloons
        #         remaining = dp(nums without nums[i])
        #         max_coins = max(max_coins, gain + remaining)
            
        #     save dp_state and the result into memo_dict
        #     return max_coins
        # }

        # function maxCoin(nums) {
        #     nums = [1] + nums + [1] // add fake balloons
        #     return dp(nums, empty_memo_dict)
        # }


# %% [markdown]
# ### Solution 2, Recursion + Memo +  Divide & Conquer
# Solution description
# - Time Complexity: O(N)
# - Space Complexity: O(N)

# %%
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # special case all the numbers in nums are the same
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # handle edge case
        # add sentinel ballons to the left and right
        nums = [1] + nums + [1]

        @lru_cache(None)  # memoization
        def dp(left, right):
            # maximum if we burst all nums[left]...nums[right], inclusive
            if right - left < 0:
                return 0
            result = 0
            # find the last burst one in nums[left]...nums[right]
            for i in range(left, right + 1):
                # nums[i] is the last burst one
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                # nums[i] is fixed, recursively call left side and right side
                remaining = dp(left, i - 1) + dp(i + 1, right)
                # update the result
                result = max(result, remaining + gain)
            return result

        # we can not burst the first one and the last one
        # since they are both fake balloons added by ourselves
        return dp(1, len(nums) - 2)


# %% [markdown]
# ### Solution 3, Dynamic Programming, Bottom Up
# Solution description
# - Time Complexity: O(N)
# - Space Complexity: O(N)

# %%
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # special case
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # handle edge case
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] represents
        # maximum if we burst all nums[left]...nums[right], inclusive
        dp = [[0] * n for _ in range(n)]

        # do not include the first one and the last one
        # since they are both fake balloons added by ourselves and we can not
        # burst them
        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                # find the last burst one in nums[left]...nums[right]
                for i in range(left, right + 1):
                    # nums[i] is the last burst one
                    gain = nums[left - 1] * nums[i] * nums[right + 1]
                    # recursively call left side and right side
                    remaining = dp[left][i - 1] + dp[i + 1][right]
                    # update
                    dp[left][right] = max(remaining + gain, dp[left][right])
        # burst nums[1]...nums[n-2], excluding the first one and the last one
        return dp[1][n - 2]
