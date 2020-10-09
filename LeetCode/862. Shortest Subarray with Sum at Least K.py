from typing import List
from collections import deque

"""
Problem Name: 862. Shortest Subarray with Sum at Least K

Problem Section: Array, Deque

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
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque
"""

""" 93 / 93 test cases passed.
	Status: Accepted
Runtime: 808 ms
Memory Usage: 21 MB """

# Solution techniques are Monotmic Queue and Prefix Sum array

# Time complexity : O(N) Space complexity : O(N)
# Complexity Analysis
# Time Complexity: O(N), where NNN is the length of A.
# Space Complexity: O(N).


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        arraylen = len(A)
        prefixsum = [0]

        for no in A:
            prefixsum.append(prefixsum[-1]+no)

        # print(prefixsum)

        ans = arraylen+1

        monoq = deque()

        for i, pval in enumerate(prefixsum):

            while monoq and pval <= prefixsum[monoq[-1]]:
                monoq.pop()

            while monoq and pval-prefixsum[monoq[0]] >= K:
                ans = min(ans, i-monoq.popleft())

            monoq.append(i)

        return ans if ans < arraylen+1 else -1


myobj = Solution()
inpt = [2, -1, 2]
K = 3
print(myobj.shortestSubarray(inpt, K))
