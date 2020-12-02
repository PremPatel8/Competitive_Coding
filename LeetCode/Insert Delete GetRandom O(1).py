from typing import List

"""
Problem Name: Insert Delete GetRandom O(1)

Problem URL: https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/813/

Problem Section: Design, Set, Data Structures

Problem Statement:
Implement the RandomizedSet class:

    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

Follow up: Could you implement the functions of the class with each function works in average O(1) time?

Constraints:
-231 <= val <= 231 - 1
At most 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

Resources:

runtime: 
18 / 18 test cases passed.
	Status: Accepted
Runtime: 104 ms
Memory Usage: 18.5 MB

18 / 18 test cases passed.
	Status: Accepted
Runtime: 96 ms
Memory Usage: 18.4 MB
"""

# Solution techniques are use List with Dict

# Time complexity : O(1) Space complexity : O(n)


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            idx = self.pos[val] # get val index in list
            last = self.nums[-1] # get the last addition
            self.nums[idx] = last # overwrite val index with last addition
            self.pos[last] = idx # update the last addition's index to it's new spot
            self.nums.pop() # get rid of the last addition from it's original spot
            del self.pos[val] # we don't need pop-or-default semantics here, del will work
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
