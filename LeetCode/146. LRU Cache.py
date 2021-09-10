from typing import List
from collections import OrderedDict

"""
Problem Name: 146. LRU Cache

Problem URL: https://leetcode.com/problems/lru-cache/

Problem Section: Design, Doubly Linked List, Dict, Ordered Dict

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

 

Constraints:

    1 <= capacity <= 3000
    0 <= key <= 3000
    0 <= value <= 104
    At most 3 * 104 calls will be made to get and put.



Resources:
https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict).
https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList

runtime: 
18 / 18 test cases passed.
	Status: Accepted
Runtime: 148 ms
Memory Usage: 23.4 MB
"""

# Solution techniques are OrderedDict with move_to_end and popitem FIFO order

# Time complexity : Get & Put O(1) Space complexity : O(n) number of key, val pairs


""" class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyDict = OrderedDict()

    def get(self, key: int) -> int:
        res = -1

        if key in self.keyDict:
            self.keyDict.move_to_end(key)
            res = self.keyDict[key]

        return res

    def put(self, key: int, value: int) -> None:
        if key in self.keyDict:
            del self.keyDict[key]
        else:
            if len(self.keyDict) >= self.capacity:
                self.keyDict.popitem(last=False)

        self.keyDict[key] = value """


# Solution techniques are Dict with Key as key and value as Doubly Linked List node &
# Doubly Linked List to maintain LRU order of Nodes with LRU node at tail and most recently used node at head

# Time complexity : Get & Put O(1) Space complexity : O(n) number of key, val pairs


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyDict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        head_next = self.head.next
        node.next = head_next
        head_next.prev = node
        self.head.next = node
        node.prev = self.head

    def removeNode(self, node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def moveNodeToFront(self, node):
        self.removeNode(node)
        self.addNode(node)

    def get(self, key: int) -> int:
        res = -1

        if key in self.keyDict:
            node = self.keyDict[key]
            res = node.val
            self.moveNodeToFront(node)

        return res

    def put(self, key: int, value: int) -> None:
        if key in self.keyDict:
            node = self.keyDict[key]
            node.val = value
            self.moveNodeToFront(node)
        else:
            newNode = Node(key, value)

            if len(self.keyDict) >= self.capacity:
                del self.keyDict[self.tail.prev.key]
                self.removeNode(self.tail.prev)

            self.keyDict[key] = newNode
            self.addNode(newNode)


# Your LRUCache object will be instantiated and called as such:
# inpt = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

# obj = LRUCache(capacity)

# param_1 = obj.get(key)

# obj.put(key, value)
