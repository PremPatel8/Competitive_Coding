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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        strLen = len(s)
        wordDict = set(wordDict)
        dp = [False] * (strLen+1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True

        for i in range(strLen):
            if dp[i]:
                for j in range(i, strLen):
                    if dp[i] and s[i: j+1] in wordDict:
                        dp[j+1] = True

        return dp[-1]


myobj = Solution()
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

# s = "leetcode"
# wordDict = ["leet", "code"]
print(myobj.wordBreak(s, wordDict))
