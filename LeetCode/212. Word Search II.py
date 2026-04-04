# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: .venv (3.13.2)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## 212. Word Search II
# - Description:
#   <blockquote>
#   [212. Word Search II](https://leetcode.com/problems/word-search-ii/) Given an `m x n` `board` of characters and a list of strings `words`, return  *all words on the board* .
#  
# Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#  
# **Example 1:**
# ![Image](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)
#  
# **Input:** board = `["o", "a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]`, words = ["oath","pea","eat","rain"]
# **Output:** ["eat","oath"]
#  
# **Example 2:**
# ![Image](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)
#  
# **Input:** board = `["a", "b"],["c","d"]`, words = ["abcb"]
# **Output:** []
#  
# **Constraints:**
#  
# - `m == board.length`
# - `n == board[i].length`
# - `1 <= m, n <= 12`
# - `board[i][j]` is a lowercase English letter.
# - `1 <= words.length <= 3 * 104`
# - `1 <= words[i].length <= 10`
# - `words[i]` consists of lowercase English letters.
# - All the strings of `words` are unique.
#   </blockquote>
#
# - URL: [Problem_URL](https://leetcode.com/problems/word-search-ii/description/)
#
# - Topics: Backtracking, Trie
#
# - Difficulty: Hard
#
# - Resources: example_resource_URL

# %% [markdown]
# ### Solution 1, Trie-Guided Backtracking with Incremental Leaf Pruning optimization
#
# W = number of words, 
# L = max word length
# M = No of Rows
# N = No of Cols
# C = Total No of Cells AKA M*N
#
# - Time Complexity: O(W·L + M·N·4·3^(L-1)) ~ O(W*L + C*4*3^(L-1))
# 1. Trie Construction → O(W · L)
#
#     W = number of words, L = max word length
#     Each word is inserted character by character
#
# 2. Backtracking → O(M · N · 4 · 3^(L-1))
#
#     M·N = every cell is a potential starting point
#     From the first cell: 4 possible directions
#     From each subsequent cell: at most 3 directions (one cell is marked #, eliminating going back)
#     Max depth = L (max word length — trie limits how deep we go)
#
# A word of length L requires L steps on the board. The first first step has 4 possible directions we can go in, the next step onwards you only have 3 directions as the previous cell we moved from is marked as '#' to prevent going back to it, so every step after the first will have 3 directions and we will take L-1 such steps for a word of length L.
#
# - Space Complexity: O(W · L)  
# Trie nodes - O(W · L)  
# Recursion call stack - O(L) — The recursion stack goes at most L levels deep, depth bounded by max word length  
# matchedWords output - O(W)
#
# Trie dominates → O(W · L)
#
# Worth noting: the leaf pruning optimization progressively shrinks the trie during search, improving practical time and space performance beyond the theoretical worst case, though it doesn't change the asymptotic bounds.
# Solution description

# %% [markdown]
# # Interview Script
#
# Here's a script structured around the 4 phases of a strong interview explanation: restate, approach, walkthrough, complexity.
#
# ---
#
# ## Phase 1 — Restate the Problem (30 seconds)
#
# > "So we're given a 2D board of characters and a list of words, and we need to return all words that can be found on the board. A word is valid if we can trace it through sequentially adjacent cells — up, down, left, right — without reusing the same cell twice within a single word."
#
# ---
#
# ## Phase 2 — Establish the Naive Approach and Its Problem (1 minute)
#
# > "The brute force would be: for each word, run a DFS from every cell on the board trying to match it. That works for a single word — which is basically Word Search I — but here we could have tens of thousands of words. So we'd be repeating the entire board traversal once per word, which blows up the time complexity."
#
# > "The key observation is: when I'm doing DFS from a cell and building a path character by character, I'm building prefixes. Instead of checking one word at a time, I want to check all words simultaneously as I traverse the board. That way a single DFS pass can match multiple words at once."
#
# > "That's exactly what a Trie gives me. If I preload all the words into a Trie, then as I walk the board I walk the Trie in parallel. The moment the current prefix doesn't exist in the Trie, I prune that entire path immediately — no point going deeper. This collapses checking all words into a single O(1) Trie lookup at each step."
#
# ---
#
# ## Phase 3 — Explain the Implementation (2-3 minutes)
#
# ### Building the Trie
#
# > "First I build the Trie from the word list. Each node has a children dictionary and a word field. I store the entire word at the terminal node — not just a boolean flag — so that when I find a match during DFS I can directly append it to results without reconstructing the string through concatenation at every step."
#
# ### The Backtracking Function
#
# > "The backtracking function takes row, col, and parent — where parent is the Trie node one level above the current cell's character. At the top of the function I extract currNode as parent.children[letter], which is the Trie node corresponding to the current cell."
#
# > "If currNode.word is set, I've found a complete word. I append it to results and immediately reset currNode.word to None — this prevents the same word from being added again if a different path on the board reaches the same sequence of characters."
#
# > "Then I mark the current cell as visited by overwriting it with a sentinel character, hash, so that neighbors during this DFS path can't reuse it. This is the in-place visited tracking — no separate visited set needed."
#
# > "Then I iterate over the four neighbors. For each one I apply two pruning checks before making the recursive call: first, is it in bounds? Second, is that neighbor's character a child of currNode in the Trie? If either check fails I skip it. This guard-at-dispatch style avoids making a recursive call just to immediately return — the pruning fires before the stack frame is created."
#
# > "After recursing into all neighbors, I restore the cell back to its original letter — that's the backtrack step."
#
# > "Then comes the Trie pruning optimization: if currNode has no children left, it means no further words can ever extend from this node. So I remove it from parent's children. This progressively shrinks the Trie as the search proceeds, so later DFS calls from other starting cells hit smaller Trie nodes and prune earlier."
#
# ### The Outer Loop
#
# > "Finally I iterate over every cell on the board. Before calling backtracking I do one upfront check: is this cell's letter even in root's children? If not, no word starts with that character, so I skip it entirely. This avoids entering backtracking from a dead start."
#
# ---
#
# ## Phase 4 — Complexity (1 minute)
#
# > "For time complexity: building the Trie is O(W times L) where W is the number of words and L is the max word length. The DFS is harder to bound tightly. From each cell we explore at most 4 directions, and at each step we go at most L levels deep since the Trie caps the depth at the longest word. So in the worst case it's O(N times M times 4 times 3 to the L minus 1) — the 3 comes from the fact that at each step after the first, one of the 4 neighbors is where we came from and is already marked visited. In practice the Trie pruning cuts this down significantly."
#
# > "For space: the Trie holds all characters across all words, so O(W times L). The recursion stack goes at most L levels deep, so O(L) call stack space. The board modification is in-place so no extra space there."
#
# ---
#
# ## Handling Follow-up Questions
#
# A few likely pushbacks and how to address them:
#
# **"Why store the whole word at the node instead of just a boolean?"**
# > "To avoid string concatenation during traversal. If I only stored a boolean I'd have to carry the current string as a parameter and build it character by character. Storing the word directly makes the backtracking function simpler and the lookup O(1)."
#
# **"Why use in-place board marking instead of a visited set?"**
# > "It's more space efficient — no extra O(N times M) set. And since I restore the cell after backtracking, the board is clean for subsequent DFS calls from other starting cells."
#
# **"When does the Trie pruning actually help?"**
# > "Most when words share long common prefixes. Once a word is fully matched and its terminal node becomes a leaf, it gets pruned. DFS calls from other cells that would have traversed down to that node now stop earlier. In dense boards with many short words, the Trie can shrink substantially mid-search."
#

# %%
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        """
        Why store the whole word at the node instead of just a is_node boolean
        To avoid string concatenation during traversal. If I only stored a boolean I'd have to carry the current string as a parameter and build it character by character. 
        Storing the word directly makes the backtracking function simpler and the lookup O(1).
        """
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TrieNode()  # replaces setdefault()
                node = node.children[letter]
            # we store the entire word to keep the backtracking function simpler and cleaner, to avoid string concatenation at every step to build the word during traversal
            node.word = word

        rowSize = len(board)
        colSize = len(board[0])
        matchedWords = []

        """
        The key insight: when you're doing DFS from a cell, you're building prefixes one character at a time. Instead of checking one word at a time, you want to check all words simultaneously as you traverse the grid.
        This is exactly what a Trie is for.
        
        Build a Trie from all the words first. Now when you do DFS on the board, at each step you move through the Trie simultaneously. If the current path's prefix doesn't exist in the Trie, you prune the entire subtree immediately — no point going deeper.
        This collapses the "check against all words" problem into a single O(1) Trie lookup per step.
        The Trie node becomes your state at each recursion level. Instead of carrying the current string around, you carry a Trie node pointer — if you can move to the next node, the prefix is valid.
        """
        
        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent.children[letter]

            if currNode.word:
                matchedWords.append(currNode.word)
                # reset to avoid duplicate words, aka once we match a word and add it to matchedWords we do not want that word to be matched again through a different path on the board
                currNode.word = None
                # we continue with the backtracking to find any longer words extending from here

            board[row][col] = "#"

            for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                # We skip any row, col values that are out of bound of the matrix
                if newRow < 0 or newRow >= rowSize or newCol < 0 or newCol >= colSize:
                    continue
                # we skip going down any paths that are not the next character from the current character, aka child nodes of the currNode, aka one of the possible words that extends from this prefix onwards
                if board[newRow][newCol] not in currNode.children:
                    continue
                # currNode is not updated here because the recursion handles node traversal incrementally, 
                # as currNode is set at the start of each call based on the current parent and the letter at (row, col).
                backtracking(newRow, newCol, currNode)

            # After recursing into all neighbors, I restore the cell back to its original letter — that's the backtrack step
            board[row][col] = letter

            # Optimization - Gradually prune the nodes in Trie during the backtracking
            # For a leaf node in Trie, once we traverse it (i.e. find a matched word), we would no longer need to traverse it again. As a result, we could prune it out from the Trie.
            # we only prune when currNode.children is empty, meaning truly no further words can extend from that node.
            if not currNode.children:
                parent.children.pop(letter)

        # Iterate through each cell of the board
        for row in range(rowSize):
            for col in range(colSize):
                # Only proceed if the current cell letter is in the Trie, aka part of the words list
                if board[row][col] in root.children:
                    backtracking(row, col, root)

        return matchedWords


# %%
sol = Solution()

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
expected = ["oath","eat"]

result = sol.findWords(board, words)
print(f"result = {result}")
print(result == expected)
