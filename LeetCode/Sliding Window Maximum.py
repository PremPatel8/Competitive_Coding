from typing import List
from collections import deque

"""
Problem Name: Sliding Window Maximum

Problem Section:

Problem Statement:
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window
moves right by one position.

Return the max sliding window.

Our task is to return a list of integers that contains the largest element from each window.

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


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Index in mono queue increasing (lowest / initial index to last index)
        # Values of array at those index decreasing (Highest value to lowest value left to right)
        # Leftmost index value in mono queue corresponds to highest value in current window so far
        # Pop the left most index value in mono queue if it's outside the current elements windows leftmost index
        # Starting from right side check for any value less than current array num and pop them
        
        """
        Core Idea:
        We maintain a deque (double-ended queue) that stores indices of elements in decreasing order of their values. The front of the deque always contains the index of the maximum element in the current window.
        
        Why This Works
        The deque maintains two critical properties:
        Front has the maximum: dq[0] always points to the largest element in the current window
        Monotonically decreasing: Elements decrease in value from front to back
        Recent elements beat older equal elements: If a newer element is >= an older one, we remove the older one
        
        If an older element is smaller than the current element, it can never be the maximum of any future window (because the current element is both larger and will stay in the window longer).
        """

        dq = deque()  # stores indices
        output = []
        
        for i in range(len(nums)):
            # Step 1: Remove indices outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # Step 2: Remove smaller elements (they'll never be max)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Step 3: Add current index
            dq.append(i)
            
            # Step 4: Record the max (front of deque) once window is full
            if i >= k - 1:
                output.append(nums[dq[0]])
        
        return output
    
    
    """
    Max heap solution

    Time complexity: O(nlog⁡n)
    Space complexity: O(n)

    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output


myobj = Solution()
inpt = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = myobj.maxSlidingWindow(inpt, k)
print(res)
print(res == [3, 3, 5, 5, 6, 7])
