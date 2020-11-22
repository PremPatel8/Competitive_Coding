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
https://leetcode.com/problems/implement-trie-prefix-tree/discuss/362916/Simple-Python-solution-(beats-99-runtime-95-memory)
https://www.kite.com/python/answers/how-to-create-a-trie-in-python
https://www.geeksforgeeks.org/trie-insert-and-search/

runtime:
15 / 15 test cases passed.
	Status: Accepted
Runtime: 232 ms
Memory Usage: 33.8 MB

"""

# Solution techniques are alt size 26 char array sol

# Time complexity : O(M) Space complexity : O()
# where M is maximum string length and N is number of keys in tree
# If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N


class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.word_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            index = ord(letter)-ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]

        curr.word_end = True

    def search(self, word: str, word_search=True) -> bool:
        curr = self.root

        for letter in word:
            index = ord(letter)-ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]

        return curr.word_end if word_search else True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
