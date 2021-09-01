from typing import List
from collections import Counter
import itertools
import heapq

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
    # Bucket Sort solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums) or len(nums) == 1:
            return nums

        buckets = [[] for _ in range(len(nums) + 1)]

        Count = Counter(nums).items()

        for num, freq in Count:
            buckets[freq].append(num)

        # print(buckets)

        flat_list = []

        # for bucket_list in buckets:
        #     for num in bucket_list:
        #         flat_list.append(num)

        for bucket_list in reversed(buckets):
            flat_list.extend(bucket_list)

        # flat_list = [num for bucket_list in buckets for num in bucket_list]
        # flat_list = list(itertools.chain.from_iterable(buckets))

        # print(flat_list)

        return flat_list[:k]

    

    # Heap solution
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        print(count)
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        # return heapq.nlargest(k, count.keys(), key=count.get)

        heap = []
        heapq.heapify(heap)

        for num, freq in count.items():
            print(heap)
            print((freq, num))
            heapq.heappush(heap, (freq, num))
            # Heap elements can be tuples. This is useful for assigning comparison values
            # (such as task priorities) alongside the main record being tracked
            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)

        res = [heapq.heappop(heap)[1] for _ in range(len(heap))]

        return res


myobj = Solution()

input = [1, 1, 1, 2, 2, 3]

k = 2

print(myobj.topKFrequent(input, k))
