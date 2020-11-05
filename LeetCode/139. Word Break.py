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

# Time complexity : O(n) Space complexity : O(n)

""" 
["cats", "dog", "sand", "and", "cat"]

0 1 2 3 4 5 6 7 8
c a t s a n d o g
F F F F F F F F F
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                # does the word end at this index AND (did a word end before the start of current word OR does this curr word start from the beginning of the string)
                if word == s[i-len(word)+1 : i+1] and (dp[i-len(word)] or i-len(word) == -1):
                    dp[i] = True

        return dp[-1]


myobj = Solution()
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "leetcode"
wordDict = ["leet", "code"]
print(myobj.wordBreak(s, wordDict))
