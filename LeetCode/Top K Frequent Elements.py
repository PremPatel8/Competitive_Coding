from typing import List
from collections import Counter

"""
Problem Name: Top K Frequent Elements

Problem Section: Sorting and Searching

Problem Statement:
Given a non-empty array of integers, return the k most frequent elements.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""

""" 21 / 21 test cases passed.
	Status: Accepted
Runtime: 124 ms
Memory Usage: 18.3 MB """


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = Counter(nums).most_common(k)

        return [x[0] for x in output]


myobj = Solution()

input = [1, 1, 1, 2, 2, 3]

k = 2

print(myobj.topKFrequent(input, k))
