from typing import List
from collections import Counter

"""
Problem Name: 4Sum II

Problem Section: Array and Strings

Problem Statement:
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


Resources:

"""

""" 48 / 48 test cases passed.
	Status: Accepted
Runtime: 280 ms
Memory Usage: 34.6 MB """

# Solution techniques are

# Time complexity : O(n**2) Space complexity : O(n**2) Optimized solution using counter and list comprehension


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)


myobj = Solution()
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(myobj.fourSumCount(A, B, C, D))
