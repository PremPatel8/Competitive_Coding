from typing import List
from collections import defaultdict, deque

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
43 / 43 test cases passed.
	Status: Accepted
Runtime: 108 ms
Memory Usage: 17.8 MB
"""

# Solution techniques are Breadth First Search

# Time complexity : O(M**2 * N) Space complexity : O(M**2 * N)
""" 
Time Complexity: O(M2×N)O({M}^2 \times N)O(M2×N), where MMM is the length of each word and NNN is the total number of words in the input word list.
    For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it. Since the length of each word is MMM and we have NNN words, the total number of iterations the algorithm takes to create all_combo_dict is M×NM \times NM×N. Additionally, forming each of the intermediate word takes O(M)O(M)O(M) time because of the substring operation used to create the new string. This adds up to a complexity of O(M2×N)O({M}^2 \times N)O(M2×N).
    Breadth first search in the worst case might go to each of the NNN words. For each word, we need to examine MMM possible intermediate words/combinations. Notice, we have used the substring operation to find each of the combination. Thus, MMM combinations take O(M2)O({M} ^ 2)O(M2) time. As a result, the time complexity of BFS traversal would also be O(M2×N)O({M}^2 \times N)O(M2×N).
Combining the above steps, the overall time complexity of this approach is O(M2×N)O({M}^2 \times N)O(M2×N).

Space Complexity: O(M2×N)O({M}^2 \times N)O(M2×N).
    Each word in the word list would have MMM intermediate combinations. To create the all_combo_dict dictionary we save an intermediate word as the key and its corresponding original words as the value. Note, for each of MMM intermediate words we save the original word of length MMM. This simply means, for every word we would need a space of M2{M}^2M2 to save all the transformations corresponding to it. Thus, all_combo_dict would need a total space of O(M2×N)O({M}^2 \times N)O(M2×N).
    Visited dictionary would need a space of O(M×N)O(M \times N)O(M×N) as each word is of length MMM.
    Queue for BFS in worst case would need a space for all O(N)O(N)O(N) words and this would also result in a space complexity of O(M×N)O(M \times N)O(M×N).
Combining the above steps, the overall space complexity is O(M2×N)O({M}^2 \times N)O(M2×N) + O(M∗N)O(M * N)O(M∗N) + O(M∗N)O(M * N)O(M∗N) = O(M2×N)O({M}^2 \times N)O(M2×N) space.
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Queue for BFS
        queue = deque([(beginWord, 1)])

        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}

        while queue:
            current_word, level = queue.popleft()

            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))

                all_combo_dict[intermediate_word] = []

        return 0


# myobj = Solution()
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# print(myobj.ladderLength(beginWord, endWord, wordList))


def test_ladderLength():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    output = 5
    assert Solution().ladderLength(beginWord, endWord, wordList) == output
