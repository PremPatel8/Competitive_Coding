from typing import List
from collections import deque

"""
Problem Name: 862. Shortest Subarray with Sum at Least K

Problem URL: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Problem Section: Array, Monotonic Queue, Prefix Sum, Sliding Window

Problem Difficulty: Hard

Problem Statement:
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.
 

Example 1:
Input: A = [1], K = 1
Output: 1

Example 2:
Input: A = [1,2], K = 4
Output: -1

Example 3:
Input: A = [2,-1,2], K = 3
Output: 3

Note:
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9


Resources:
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/189039/Detailed-intuition-behind-Deque-solution
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary
https://medium.com/@gregsh9.5/monotonic-queue-notes-980a019d5793
https://1e9.medium.com/monotonic-queue-notes-980a019d5793
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/1132081/Pictures-to-show-step-by-step-optimization-from-O(n)-to-O(n)-without-jump-thinking
"""

""" 93 / 93 test cases passed.
	Status: Accepted
Runtime: 808 ms
Memory Usage: 21 MB """

# Solution techniques are Monotonic Queue and Prefix Sum array used for sliding window technique

# Time complexity : O(N) Space complexity : O(N)
# Complexity Analysis
# Time Complexity: O(N), where NNN is the length of A.
# Space Complexity: O(N).

""" 
What makes this problem hard is that we have negative values. 

Recall of the Sliding window solution in a positive array

The Sliding window solution finds the subarray we are looking for in a linear time complexity. 
The idea behind it is to maintain two pointers: start and end, moving them in a smart way to avoid examining all possible values 0<=end<=n-1 and 0<=start<=end (to avoid brute force).

What it does is:
    Incremeting the end pointer while the sum of current subarray (defined by current values of start and end) is smaller than the target.
    Once we satisfy our condition (the sum of current subarray >= target) we keep incrementing the start pointer until we violate it (until sum(array[start:end+1]) < target).
    Once we violate the condition we keep incrementing the end pointer until the condition is satisfied again and so on.

The reason why we stop incrementing start when we violate the condition is that we are sure we will not satisfy it again if we keep incrementing start. 
In other words, if the sum of the current subarray start -> end is smaller than the target then the sum of start+1 -> end is neccessarily smaller than the target. (positive values)
The problem with this solution is that it doesn't work if we have negative values, this is because of the sentence above Once we "violate" the condition we stop incrementing start.

Problem of the Sliding window with negative values

Now, let's take an example with negative values nums = [3, -2, 5] and target=4. Initially start=0, we keep moving the end pointer until we satisfy the condition, 
here we will have start=0 and end=2. Now we are going to move the start pointer start=1. The sum of the current subarray is -2+5=3 < 4 so we violate the condition. 
However if we just move the start pointer another time start=2 we will find 5 >= 4 and we are satisfying the condition. And this is not what the Sliding window assumes.
"""

""" 
In this solution, we are using the prefix sum array as the array over which the right pointer iterates and
the monotonic queue as the array over which the left pointer iterates in the form of the left most 0th positional value in the queue
this way we define the left and right bounds of our sliding window

What does the Deque store :
The deque stores the possible values of the left pointer. Unlike the sliding window, values of the left variable will not necessarily be contiguous.

Why is it increasing :
So that when we move the left pointer and we violate the condition, we are sure we will violate it if we keep taking the other values from the Deque. 
In other words, if the sum of the subarray from left=first value in the deque to end is smaller than target, 
then the sum of the subarray from left=second value in the deque to end is necessarily smaller than target.
So because the Deque is increasing (B[d[0]] <= B[d[1]]), we have B[i] - B[d[0]] >= B[i] - B[d[1]], 
which means the sum of the subarray starting from d[0] is greater than the sum of the sub array starting from d[1].

Why do we have a prefix array and not just the initial array like in sliding window :
Because in the sliding window when we move start (typically when we increment it) we can just substract nums[start-1] from the current sum and we get the sum of the new subarray. 
Here the value of the start is jumping and one way to compute the sum of the current subarray in a constant time is to have the prefix array.

Why using Deque and not simply an array :
We can use an array, however we will find ourselves doing only three operations:
1- remove_front : when we satisfy our condition and we want to move the start pointer
2- append_back : for any index that may be a future start pointer
3- remove_back : When we are no longer satisfying the increasing order of the array
Deque enables doing these 3 operations in a constant time.
"""


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        arraylen = len(nums)
        prefixsum = [0]

        for no in nums:
            prefixsum.append(prefixsum[-1]+no)

        print(prefixsum)

        # We Want smallest y-x with Py - Px >= k
        # N+1 is impossible
        ans = arraylen+1

        # Monoq, deque stores possible values of the left pointer
        # Unlike the sliding window, values of the left variable will not necessarily be contiguous.
        monoq = deque()

        for right, pval in enumerate(prefixsum):

            while monoq and prefixsum[monoq[-1]] >= pval:
                monoq.pop()

            while monoq and pval-prefixsum[monoq[0]] >= k:
                ans = min(ans, right-monoq.popleft())

            monoq.append(right)

        return ans if ans < arraylen+1 else -1


myobj = Solution()
# inpt = [2, -1, 2]
# K = 3

inpt = [84, -37, 32, 40, 95]
K = 167
# op = 3
print(myobj.shortestSubarray(inpt, K))
