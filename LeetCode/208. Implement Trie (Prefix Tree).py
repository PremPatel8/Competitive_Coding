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
https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58953/AC-Python-solution-using-defaultdict
https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58927/Compact-Python-solution

runtime:
15 / 15 test cases passed.
	Status: Accepted
Runtime: 136 ms
Memory Usage: 27.8 MB

"""

# Solution techniques are efficient nested dict solution

# Time complexity : O() Space complexity : O()


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]

        curr["."] = True

    def search(self, word: str, word_search=True) -> bool:
        curr = self.root

        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]

        return "." in curr if word_search else True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
