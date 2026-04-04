# %% [markdown]
"""
## [72. Edit Distance](https://leetcode.com/problems/edit-distance/)

<blockquote>
    Given two strings `word1` and `word2`, return  *the minimum number of operations required to convert `word1` to `word2`* .
     
    You have the following three operations permitted on a word:
     
    - Insert a character
    - Delete a character
    - Replace a character
     
    **Example 1:**
    **Input:** word1 = "horse", word2 = "ros"
    **Output:** 3
    **Explanation:** 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
     
    **Example 2:**
    **Input:** word1 = "intention", word2 = "execution"
    **Output:** 5
    **Explanation:** 
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
     
    **Constraints:**
     
    - `0 <= word1.length, word2.length <= 500`
    - `word1` and `word2` consist of lowercase English letters.
</blockquote>  

- Topics: Recursion+Memo, DP

- Difficulty: Medium/Hard
"""


# %% [markdown]
"""
### Approach 1: Naive Recursion

Let K be the length of string word1 and N be the length of string word2. Let M=max(K,N).
- Time Complexity: O(3**M)
    - The time complexity is exponential. For every pair of word1 and word2, if the characters do not match, we recursively explore three possibilities. In the worst case, if none of the characters match, we will end up exploring O(3M) possibilities.

- Space Complexity: O(M)
    - The recursion uses an internal call stack equal to the depth of the recursion tree. The recursive process will terminate when either word1 or word2 is empty.
"""

# %% [markdown]
"""
In the recursive formulation for Edit Distance, **`word1Index` and `word2Index` represent the *lengths* of the current prefixes being compared** (i.e., `word1[0:word1Index]` and `word2[0:word2Index]`).
This is critical for interpreting the recursive calls:

🔹 **Insert operation**  
`minDistanceRecur(word1, word2, word1Index, word2Index - 1)`  
→ *Why?* Insert `word2[word2Index-1]` **at the end** of `word1`'s current prefix. This matches the last character of `word2`'s prefix, so we:  
- Keep `word1`'s prefix length unchanged (`word1Index` remains)  
- Reduce `word2`'s prefix length by 1 (`word2Index - 1`)  
*(Conceptually: "Solve for converting full `word1[0:i]` to `word2[0:j-1]`, then insert `word2[j-1]`")*

🔹 **Delete operation**  
`minDistanceRecur(word1, word2, word1Index - 1, word2Index)`  
→ Delete last character of `word1`'s prefix (`word1[word1Index-1]`). Now solve for:  
- Shorter `word1` prefix (`word1Index - 1`)  
- Full `word2` prefix (`word2Index` unchanged)

🔹 **Replace operation**  
`minDistanceRecur(word1, word2, word1Index - 1, word2Index - 1)`  
→ Replace `word1[word1Index-1]` with `word2[word2Index-1]`. Both last characters now match, so solve for the prefixes *without* these last characters.

💡 **Key insight**:  
The recursion **does not track physical insertion positions** (like "insert at index 2"). Instead, it leverages *optimal substructure*:  
- All operations are conceptually applied to the **end of the current prefix**  
- Shifting behavior is abstracted away by the state transition  
- The DP/recursion guarantees minimal cost regardless of *where* operations occur physically  

✅ **Your example**: `word1="abc"`, `word2="abe"` at state `(3,3)`  
- Insert path: `(3,2)` → convert `"abc"` → `"ab"` (cost=1: delete `'c'`), +1 insert = **2**  
- Replace path: `(2,2)` → `"ab"`→`"ab"` (cost=0), +1 replace = **1** (optimal)  

This abstraction is why the recurrence works! Does seeing how the *prefix lengths* drive the state transitions clarify the recursion logic? 😊
"""


# %%
class Recursive:
    def minDistance(self, word1: str, word2: str) -> int:
        # calculate the distance between two words using recursion
        return self.minDistanceRecur(word1, word2, len(word1), len(word2))

    def minDistanceRecur(
        self, word1: str, word2: str, word1Index: int, word2Index: int
    ) -> int:
        # base cases
        if (
            word1Index == 0
        ):  # if word1 is empty, the minimum distance is the length of word2
            return word2Index
        if (
            word2Index == 0
        ):  # if word2 is empty, the minimum distance is the length of word1
            return word1Index
        # if the characters are same, continue with next pair of characters
        if word1[word1Index - 1] == word2[word2Index - 1]:
            return self.minDistanceRecur(
                word1, word2, word1Index - 1, word2Index - 1
            )
        else:
            # calculate the cost of insert, delete, and replace operations
            
            # Conceptually: "Solve for converting full word1[0:i] to word2[0:j-1], then insert word2[j-1]"
            insertOperation = self.minDistanceRecur(
                word1, word2, word1Index, word2Index - 1
            )

            # Delete last character of word1's prefix (word1[word1Index-1]). Now solve for:
            # Shorter word1 prefix (word1Index - 1)
            # Full word2 prefix (word2Index unchanged)
            deleteOperation = self.minDistanceRecur(
                word1, word2, word1Index - 1, word2Index
            )
            
            # Replace word1[word1Index-1] with word2[word2Index-1]. Both last characters now match, so solve for the prefixes without these last characters.
            replaceOperation = self.minDistanceRecur(
                word1, word2, word1Index - 1, word2Index - 1
            )
            # return the minimum cost
            return min(insertOperation, deleteOperation, replaceOperation) + 1

# %% [markdown]
"""
### Approach 2: Recursion+Memoization, Top-Down Dynamic Programming

Let M be the length of string word1 and N be the length of string word2.

- Time Complexity: O(M⋅N)
    - As the memoization approach uses the cache, for every combination of word1 and word2 the result is computed only once.

- Space Complexity: O(M⋅N)
    - The space is for the additional 2-dimensional array memo of size (M⋅N).
"""

# %%
class Recursion_Memo:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [
            [None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]

        def minDistanceRecur(word1, word2, word1Index, word2Index):
            if word1Index == 0:
                return word2Index
            if word2Index == 0:
                return word1Index
            if memo[word1Index][word2Index] is not None:
                return memo[word1Index][word2Index]
            minEditDistance = 0
            if word1[word1Index - 1] == word2[word2Index - 1]:
                minEditDistance = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index - 1
                )
            else:
                insertOperation = minDistanceRecur(
                    word1, word2, word1Index, word2Index - 1
                )
                deleteOperation = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index
                )
                replaceOperation = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index - 1
                )
                minEditDistance = (
                    min(insertOperation, deleteOperation, replaceOperation) + 1
                )
            memo[word1Index][word2Index] = minEditDistance
            return minEditDistance

        return minDistanceRecur(word1, word2, len(word1), len(word2))
    

# %% [markdown]
"""
### Approach 3: Bottom-Up Dynamic Programming: Tabulationnotebook-as-script workflow (

Let M be the length of string word1 and N be the length of string word2.

- Time Complexity: O(M⋅N)
    - In the nested for loop, the outer loop iterates M times, and the inner loop iterates N times.

Thus, the time complexity is O(M⋅N).

- Space Complexity: O(M⋅N)
    - The space is for the additional 2-dimensional array dp of size (M⋅N).
"""

# %%
class Dp:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Length = len(word1)
        word2Length = len(word2)
        
        if word1Length == 0:
            return word2Length
        if word2Length == 0:
            return word1Length
        
        dp = [[0 for _ in range(word2Length + 1)] for _ in range(word1Length + 1)]
        
        for word1Index in range(1, word1Length + 1):
            dp[word1Index][0] = word1Index
        
        for word2Index in range(1, word2Length + 1):
            dp[0][word2Index] = word2Index
        
        for word1Index in range(1, word1Length + 1):
            for word2Index in range(1, word2Length + 1):
                if word2[word2Index - 1] == word1[word1Index - 1]:
                    dp[word1Index][word2Index] = dp[word1Index - 1][word2Index - 1]
                else:
                    dp[word1Index][word2Index] = (
                        min(
                            dp[word1Index - 1][word2Index],
                            dp[word1Index][word2Index - 1],
                            dp[word1Index - 1][word2Index - 1],
                        )
                        + 1
                    )
        return dp[word1Length][word2Length]

# %% [markdown]
# ### Test Area
# %%
# Now you can test both side-by-side without them clashing
print("Brute/Naieve:", Recursive().minDistance("horse", "ros")) # Expected: 3
print("Good:", Recursion_Memo().minDistance("horse", "ros")) # Expected: 3
print("Optimal:", Dp().minDistance("horse", "ros")) # Expected: 3

