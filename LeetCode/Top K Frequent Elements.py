from typing import List
from collections import Counter
import itertools

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

# Using bucket sort to get the elements sorted by increasing frequency (element with the highest frequency at the end)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums) or len(nums) == 1:
            return nums

        bucket = [[] for _ in range(len(nums) + 1)]

        Count = Counter(nums).items()

        for num, freq in Count:
            bucket[freq].append(num)

        # flat_list = [item for sublist in bucket for item in sublist]
        flat_list = list(itertools.chain.from_iterable(bucket))

        return flat_list[::-1][:k]


myobj = Solution()

input = [1, 1, 1, 2, 2, 3]

k = 2

print(myobj.topKFrequent(input, k))
