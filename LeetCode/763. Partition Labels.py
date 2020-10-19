from typing import List
from collections import defaultdict

"""
Problem Name: 763. Partition Labels

Problem URL: https://leetcode.com/problems/partition-labels/

Problem Section: Greedy, Array

Problem Statement:
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

 

Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.


Resources:

runtime: 
116 / 116 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14.3 MB

"""

# Solution techniques are

# Time complexity : O(n) Space complexity : O(1) to keep data structure last_index of not more than 26 characters.


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        left_index = right_index = 0
        last_index = defaultdict(int)

        for i, ch in enumerate(S):
            last_index[ch] = i

        for i, ch in enumerate(S):
            right_index = max(right_index, last_index[ch])

            if i == right_index:
                res.append(i-left_index+1)
                left_index = i+1

        return res


myobj = Solution()
inpt = "ababcbacadefegdehijhklij"
print(myobj.partitionLabels(inpt))
