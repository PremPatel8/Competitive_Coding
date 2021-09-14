from typing import List

"""
Problem Name: 139. Word Break

Problem URL: https://leetcode.com/problems/word-break/

Problem Section: 

Problem Statement:
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".


Resources:

runtime: 
43 / 43 test cases passed.
	Status: Accepted
Runtime: 40 ms
Memory Usage: 14.2 MB
"""

# Solution techniques are DP array

# Time complexity : O()  Space complexity : O()

""" 
["cats", "dog", "sand", "and", "cat"]

0 1 2 3 4 5 6 7 8
c a t s a n d o g
F F F F F F F F F
"""


class Solution:
    # Alt DP syntax
    """ def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        strLen = len(s)
        wordDict = set(wordDict)
        # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp = [False] * (strLen + 1)
        # 0 represents null string, which is always true
        dp[0] = True

        for i in range(strLen):
            if dp[i]:
                for j in range(i + 1, strLen + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[-1] """

    # DP Solution using two pointers
    # Keep moving right pointer to the right to check the whole string
    # And move the left pointer to breat the substring into two parts and check if they are in the dict
    # i = right, j = left
    # Time Complexity - O(n^3), There are two nested loops, and substring computation at each iteration. Overall that results in O(n^3) time complexity.
    # Space Complexity - O(n) Length of dp array is n+1

    """ We make use of dp array of size n+1, where n is the length of the given string. We also use two index pointers i and j, 
    where i refers to the length of the substring (s′) considered currently starting from the beginning, and 
    j refers to the index partitioning the current substring (s′) into smaller substrings s′(0,j) and 
    s′(j+1,i). To fill in the dp array, we initialize the element dp[0] as true, since the null string is always present in the dictionary, 
    and the rest of the elements of dp as false. 
    We consider substrings of all possible lengths starting from the beginning by making use of index i. For every such substring, 
    we partition the string into two further substrings s1′ and s2′ in all possible ways using the index j (Note that the i now refers to the ending index of s2′). 
    Now, to fill in the entry dp[i], we check if the dp[j] contains true, 
    i.e. if the substring s1′ fulfills the required criteria. If so, we further check if s2′ is present in the dictionary. 
    If both the strings fulfill the criteria, we make dp[i] as true, otherwise as false.

    s = "leetcode", wordDict = ["leet","code"]

    [   0    1      2      3      4     5      6      7      8 ]
    [   ''   l      e      e      t     c      o      d      e ]
    [True, False, False, False, True, False, False, False, True]
 """

    def wordBreak_DP(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        strLen = len(s)
        # dp[i] means s[:i] can be segmented into words in the wordDicts
        dp = [False] * (strLen + 1)
        # 0 represents null string, which is always true
        dp[0] = True

        for right in range(1, strLen + 1):
            for left in range(right):
                if dp[left] and s[left:right] in word_set:
                    dp[right] = True
                    break
        return dp[strLen]

    # Recursion with memoization solution Alt syntax
    """ def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def wordBreakMemo(s: str, word_dict: FrozenSet[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                    return True
            return False

        return wordBreakMemo(s, frozenset(wordDict), 0) """

    # Recursion with memoization solution
    # Time Complexity - O(n^3) Size of recursion tree can go up to n^2
    # Space Complexity - O(n) The depth of recursion tree can go up to n
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        return self.wordBreakMemo(s, word_set, 0, memo)

    def wordBreakMemo(self, s, word_dict, start, memo):
        if start == len(s):
            return True

        if start in memo:
            return memo[start]
        else:
            memo[start] = False

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and self.wordBreakMemo(s, word_dict, end, memo):
                memo[start] = True
                return memo[start]

        return memo[start]

    # Trie + DP solution is most optimum wwith time complexity of O(n * max(word in dict))
    # BFS solutiion has same complexity as Recursive+Memo


myobj = Solution()
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "leetcode"
wordDict = ["leet", "code"]
print(myobj.wordBreak(s, wordDict))
