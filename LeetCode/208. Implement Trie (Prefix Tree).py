from typing import List
from collections import defaultdict

"""
Problem Name: 208. Implement Trie (Prefix Tree)

Problem URL: https://leetcode.com/problems/implement-trie-prefix-tree/

Problem Section: Design, Trie, Trees, Dict

Problem Statement:
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


Resources:

runtime:
15 / 15 test cases passed.
	Status: Accepted
Runtime: 200 ms
Memory Usage: 33.3 MB

"""

# Solution techniques are My Solution using Dict

# Time complexity : O() Space complexity : O()


class TrieNode():

    def __init__(self):
        self.children = defaultdict()
        self.word_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root

        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children.get(ch)

        root.word_end = True

    def search(self, word: str) -> bool:
        root = self.root

        for ch in word:
            if ch not in root.children:
                return False
            root = root.children.get(ch)

        return True if root and root.word_end else False

    def startsWith(self, prefix: str) -> bool:
        root = self.root

        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children.get(ch)

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
