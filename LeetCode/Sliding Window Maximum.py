from typing import List
from collections import deque

"""
Problem Name: Sliding Window Maximum

Problem Section:

Problem Statement:
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:
Input: nums = [9,11], k = 2
Output: [11]

Example 5:
Input: nums = [4,-2], k = 2
Output: [4]


Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length


Resources:
"""

""" 59 / 59 test cases passed.
	Status: Accepted
Runtime: 1336 ms
Memory Usage: 30 MB """

# Solution techniques are Monotonic Queue using Deque

# Time complexity : O(n) Space complexity : O(k)


# class monoqueue:
#     m_deque = deque()

#     def push_ele(self, ele):
#         while len(monoqueue.m_deque) > 0 and monoqueue.m_deque[-1] < ele:
#             monoqueue.m_deque.pop(0)  # deQueue
#         monoqueue.m_deque.append(ele)

#     def max_ele():
#         return monoqueue.m_deque[-1]

#     def pop_ele(self, ele):


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_deque = deque()
        res = []

        for i, num in enumerate(nums):
            while mono_deque and nums[mono_deque[-1]] < num:
                mono_deque.pop()

            mono_deque.append(i)

            if mono_deque[0] == i-k:
                mono_deque.popleft()

            if i >= k-1:
                res.append(nums[mono_deque[0]])

        return res


myobj = Solution()
inpt = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = myobj.maxSlidingWindow(inpt, k)
print(res)
print(res == [3, 3, 5, 5, 6, 7])
