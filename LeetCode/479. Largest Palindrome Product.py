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
# ## 479. Largest Palindrome Product
# - Description:
#   <blockquote>
#         [479. Largest Palindrome Product](https://leetcode.com/problems/largest-palindrome-product/) Given an integer n, return  *the **largest palindromic integer** that can be represented as the product of two `n`-digits integers* . Since the answer can be very large, return it **modulo** `1337`.
#          
#         **Example 1:**
#         **Input:** n = 2
#         **Output:** 987
#         Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#          
#         **Example 2:**
#         **Input:** n = 1
#         **Output:** 9
#          
#         **Constraints:**
#          
#         - `1 <= n <= 8`
#   </blockquote>
#
# - URL: [Problem_URL](https://leetcode.com/problems/largest-palindrome-product/description/?envType=company&envId=yahoo&favoriteSlug=yahoo-all)
#
# - Topics: Math
#
# - Difficulty: Hard
#
# - Resources: example_resource_URL

# %% [markdown]
# ### Solution 1, Optimized Generate Even-Length Palindromes from n-Digit Half and Factor with Pruning
# Solution description
# - Time Complexity: O(10^(2n))
# - Space Complexity: O(1)

# %% [markdown]
# #### Key fact about factor pairs
#
# If `pal = a * b`, then one of `a, b` must be **≤ √pal** and the other **≥ √pal**.
#
# So every factor pair `(a, b)` looks like:
#
# -   either `a ≤ √pal ≤ b`
# -   or `b ≤ √pal ≤ a` (same thing, just swapped)
#
# ___
#
# #### How this applies to the descending loop
#
# Inner loop is:
#
# ```python
# for a in range(high, low - 1, -1):  # a goes from big to small
#     if a * a < pal:
#         break
#     ...
# ```
#
# Apply Code
#
# -   While `a ≥ √pal`, we _might_ still find a valid pair `(a, b)`.
# -   The moment `a < √pal` (i.e., `a * a < pal`), then:
#     -   Any factor pair with this small `a` would have `b > √pal`.
#     -   But we already checked all numbers **larger than `a`** earlier in the loop, including that possible `b`.
#     -   So if such a factor pair existed, we would have found it already when `a == b` (the larger one).
#
# Therefore, once `a < √pal`, **no new factor pairs remain to be discovered**, and we can safely `break`.

# %% [markdown]
# For `n = 1`, the problem is:
#
# -   Two 1‑digit numbers → both in `[1, 9]`
# -   We need the **largest palindrome** that can be written as `a * b` with `1 ≤ a, b ≤ 9`.
#
# Let’s reason it out:
#
# -   Max product is `9 * 9 = 81` (not a palindrome).
# -   Check which products are palindromes:
#
# 1‑digit palindromes: `1,2,3,4,5,6,7,8,9`  
# 2‑digit palindromes: `11,22,33,44,55,66,77,88,99`
#
# Now, which of these can be written as a product of two 1‑digit numbers?
#
# -   2‑digit palindromes: none of `11,22,...,99` can be written as `a * b` with both `a,b` in `[1,9]`.
# -   1‑digit palindromes: many appear (e.g., `9 = 3*3` or `1*9`, `8 = 2*4`, etc.)
#
# Among all such palindromic products, the **largest** is `9`.  
# Since `9 < 1337`, the function should return `9`.
#
# That’s why we handle `n == 1` specially:
#
# ```python
# if n == 1:
#     return 9
# ```
#
# Apply Code
#
# Then for `n ≥ 2`, the even‑length (2n‑digit) palindrome approach works.

# %%
class Solution:
    def largestPalindrome(self, n: int) -> int:
        # The following for loop only 
        if n == 1:
            return 9
        
        max_num = 10**n - 1
        min_num = 10**(n-1)
        
        # Loop from the max num to min num so we start with largest palindrome and go lower, this way the first valid palindrome we find will be the largest palindrome product and we can just return it
        for left_half in range(max_num, min_num - 1, -1):
            # create palindrome
            left_str = str(left_half)
            pal = int(left_str + left_str[::-1])
            
            # try to factor
            for factor in range(max_num, int(pal**0.5) - 1, -1):
                if pal % factor == 0:
                    other = pal // factor
                    if min_num <= other <= max_num:
                        return pal % 1337
        
        return -1


# %% [markdown]
# ### Solution 2, Generate Even-Length Palindromes from n-Digit Half and Factor with Pruning
# Solution description
# - Time Complexity: O(10^(2n))
# - Space Complexity: O(1)

# %%
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        
        min_num = 10**(n - 1)
        max_num = 10**n - 1

        for left_half in range(max_num, min_num - 1, -1):
            left_str = str(left_half)
            palindrome = int(left_str + left_str[::-1])

            for factor in range(max_num, min_num - 1, -1):
                if factor * factor < palindrome:
                    break

                if palindrome % factor == 0:
                    other_factor = palindrome // factor

                    if min_num <= other_factor <= max_num:
                        return palindrome % 1337
        
        return -1
