from typing import List
from collections import defaultdict

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
Runtime: 292 ms
Memory Usage: 55.5 MB """

# Solution techniques are

# Time complexity : O(n**2) Space complexity : O(n**2) using Dict to keep track of all A+B combination freq counts and then all -(C+D) counts 
# since a + b + c + d = 0 => a + b = -(c + d)


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB_dict = defaultdict(int)
        count = 0

        for i in A:
            for j in B:
                AB_dict[i+j] += 1

        for i in C:
            for j in D:
                count += AB_dict[-(i+j)]

        return count


myobj = Solution()
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(myobj.fourSumCount(A, B, C, D))
