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
# ## 693. Binary Number with Alternating Bits
# - Description:
#   <blockquote>
#     [693. Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/) Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#    
#     **Example 1:**
#     **Input:** n = 5
#     **Output:** true
#     **Explanation:** The binary representation of 5 is: 101
#      
#     **Example 2:**
#     **Input:** n = 7
#     **Output:** false
#     **Explanation:** The binary representation of 7 is: 111.
#      
#     **Example 3:**
#     **Input:** n = 11
#     **Output:** false
#     **Explanation:** The binary representation of 11 is: 1011.
#      
#     **Constraints:**
#      
#     - `1 <= n <= 231- 1`
#   </blockquote>
#
# - URL: [Problem_URL](https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=company&envId=yahoo&favoriteSlug=yahoo-all)
#
# - Topics: Bit Manipulation, Math
#
# - Difficulty: Easy
#
# - Resources: example_resource_URL

# %% [markdown]
# ### Solution 1, My Sol, Conver to string, iterate and compare to previous bit
#
# where W is number of bits
# - Time Complexity: O(W)
#   - However, W ≤ 32, so it is more like O(1)
# - Space Complexity: O(W)

# %%
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_str = bin(n)[2:]

        prev_bit = binary_str[0]

        for digit in binary_str[1:]:
            if digit == prev_bit:
                return False
            
            prev_bit = digit
        
        return True


# %% [markdown]
# ### Solution 2, Convert to String, iterate and compare with next index, slower than bit manipulation
#
# Why bin(n) without [2:] still works:
#
# When you call bin(n), it returns a string like '0b101' (for n=5). The string has three parts:
#
#     '0' - the first character
#     'b' - the second character
#     '101' - the actual binary digits
#
# The key insight: The prefix '0b' doesn't break the alternating check because:
#
#     '0' and 'b' are always different characters
#     'b' and the first binary digit (which is always '1' for positive integers) are always different
#     The actual binary digits are still checked correctly for alternation
#
#
# - Time Complexity: O(N)
# - Space Complexity: O(N)

# %%
class Solution():
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in range(len(bits) - 1))


# %%
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)[2:]
        
        for i in range(len(bits) - 1):
            if bits[i] == bits[i+1]:
                return False
        
        return True


# %%
class Solution():
    def hasAlternatingBits(self, n: int) -> bool:
        binary_str = bin(n)[2:]
        
        for i in range(1, len(binary_str)):
            if binary_str[i] == binary_str[i-1]:
                return False
        
        return True


# %% [markdown]
# ### Solution 3, Divide By Two, Bit Mnaipulation, most efficient, best approach to understand decimal to binary conversion
#
# Why Bit Manipulation is More Efficient:
#
#     Zero memory allocation – avoids heap allocation for string
#     Fewer operations – no string formatting/parsing
#     CPU-friendly – integer math is faster than character comparisons
#     No prefix overhead – processes exactly bit_length() iterations (vs bit_length()+2)
#
#
# where w is the number of bits in n.
# - Time Complexity: O(W)
#   - However, w≤32. so in effect it is O(1)
# - Space Complexity: O(1)

# %%
class Solution():
    def hasAlternatingBits(self, n):
        prev = n % 2
        n //= 2
        
        while n > 0:
            cur = n % 2
            if cur == prev:
                return False
            prev = cur
            n //= 2
            
        return True


# %%
class Solution():
    def hasAlternatingBits(self, n):
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2: return False
            n, cur = divmod(n, 2)
        return True


# %% [markdown]
# Div: // - QUOTIENT  
# Mod: % - REMAINDER  
#
# Decimal = 10
#
# ```
# N    D    Q  R  
# 10 / 2 =  5, 0 - LSB  
# 5  / 2 =  2, 1  
# 2  / 2 =  1, 0  
# 1  / 2 =  0, 1 - MSB
# ```
#
# Binary = 1010
#
# LSB - Least Significant Bit
# MSB - Most Significant Bit
#
# MSB (Most Significant Bit) and LSB (Least Significant Bit) denote the positions of bits in a binary number. The MSB is the leftmost bit, carrying the highest weight and maximum impact on value, while the LSB is the rightmost, carrying the lowest weight, often used to determine odd/even numbers. 

# %%
def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        # get the remainder and append it to the left of the previous binary string, because binary numbers are built from the LSB to MSB
        binary = str(n % 2) + binary
        
        # Get the quotient, make it the current number
        n = n // 2
    return binary
