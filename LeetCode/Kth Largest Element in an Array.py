from typing import List
import random
import heapq

"""
Problem Name: Kth Largest Element in an Array

Problem Section: Sorting and Searching

Problem Statement:
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

""" 32 / 32 test cases passed.
	Status: Accepted
Runtime: 76 ms
Memory Usage: 14.3 MB """

""" Analyzing the problem statement, we realize that we don't actually need to sort the entire array — we only need to rearrange its contents so that the kth element of the array is the kth largest or smallest.
In QuickSort, we pick a pivot element and move it to its correct position. We also partition the array around it. In QuickSelect, the idea is to stop at the point where the pivot itself is the kth largest element.
We can optimize the algorithm further if we don't recur for both left and right sides of the pivot. We only need to recur for one of them according to the position of the pivot.
https://www.youtube.com/watch?v=hGK_5n81drs&list=TLPQMjIwNzIwMjBd9-KgDbpTkg&index=1
"""

# O(N) best case / O(N^2) worst case running time + O(1) memory, Quick Select / QuickSort paritioning based solution


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k < 1 or nums is None:
            return 0

        if len(nums) == 1 and k <= len(nums):
            return nums[0]

        random.shuffle(nums)

        k = len(nums) - k
        lo = 0
        hi = len(nums) - 1
        while (lo < hi):
            j = self.partition(nums, lo, hi)

            if(j < k):
                lo = j + 1
            elif (j > k):
                hi = j - 1
            else:
                break

        return nums[k]

    def partition(self, nums, lo, hi):
        pivot = nums[hi]
        j = i = lo

        while (j < hi):
            if (nums[j] <= pivot):
                self.swap(nums, i, j)
                i += 1
            j += 1

        self.swap(nums, i, hi)
        return i

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


myobj = Solution()
input = [3, 2, 1, 5, 6, 4]
k = 2
# input = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
# input = [7, 6, 5, 4, 3, 2, 1]
# k = 2
print(myobj.findKthLargest(input, k))
