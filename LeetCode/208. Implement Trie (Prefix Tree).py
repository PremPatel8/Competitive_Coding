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
https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution
https://medium.com/@info.gildacademy/a-simpler-way-to-implement-trie-data-structure-in-python-efa6a958a4f2
https://albertauyeung.github.io/2020/06/15/python-trie.html

runtime:
15 / 15 test cases passed.
	Status: Accepted
Runtime: 164 ms
Memory Usage: 33.2 MB

"""

# Solution techniques are defaultdict small optimized sol

# Time complexity : O() Space complexity : O()


class TrieNode():

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            # If ch not in children defaultdict will create a new TrieNode automatically
            curr = curr.children[ch]

        curr.word_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children.get(ch)

        return True if curr and curr.word_end else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children.get(ch)

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
