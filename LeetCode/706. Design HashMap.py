"""
Problem Name: Design HashMap

Problem URL: https://leetcode.com/problems/design-hashmap/

Problem Section: Array, Hash Table, Linked List, Design, Hash Function

Problem Statement:
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

 

Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.


Resources:

runtime: 
Runtime: 264 ms, faster than 59.98% of Python3 online submissions for Design HashMap.
Memory Usage: 17.8 MB, less than 34.47% of Python3 online submissions for Design HashMap.

"""


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


""" Algorithm

For each of the methods in hashmap data structure, namely get(), put() and remove(), it all boils down to the method to locate the value that is stored in hashmap, given the key.

This localization process can be done in two steps:

    For a given key value, first we apply the hash function to generate a hash key, which corresponds to the address in our main storage. With this hash key, we would find the bucket where the value should be stored.

    Now that we found the bucket, we simply iterate through the bucket to check if the desired <key, value> pair does exist.
 """


""" 
Note that in the above implementations, we use Array to implement the bucket in Python, while we use LinkedList in Java.

Complexity Analysis

    Time Complexity: for each of the methods, the time complexity is O(NK)\mathcal{O}(\frac{N}{K})O(KN​) where NNN is the number of all possible keys and KKK is the number of predefined buckets in the hashmap, which is 2069 in our case.

        In the ideal case, the keys are evenly distributed in all buckets. As a result, on average, we could consider the size of the bucket is NK\frac{N}{K}KN​.

        Since in the worst case we need to iterate through a bucket to find the desire value, the time complexity of each method is O(NK)\mathcal{O}(\frac{N}{K})O(KN​).

    Space Complexity: O(K+M)\mathcal{O}(K+M)O(K+M) where KKK is the number of predefined buckets in the hashmap and MMM is the number of unique keys that have been inserted into the hashmap.  """