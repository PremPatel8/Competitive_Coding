from typing import List

"""
Problem Name: 127. Word Ladder

Problem URL: https://leetcode.com/problems/word-ladder/

Problem Section: 

Problem Statement:
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


Resources:

runtime: 

"""

# Solution techniques are

# Time complexity : O() Space complexity : O()


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        level = 0

        if endWord not in wordList:
            return level

        intermediate_words = {}

        for word in wordList:
            for i in range(len(word)):
                temp = word[:i]+"*"+word[i+1:]

                if temp in intermediate_words:
                    intermediate_words[temp].append(word)
                else:
                    intermediate_words[temp] = [word]

        # print(f"intermediate_state = {intermediate_words}")

        


myobj = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(myobj.ladderLength(beginWord, endWord, wordList))


""" def test_ladderLength():
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    output = 5
    assert Solution().ladderLength(beginWord, endWord, wordList) == output """
