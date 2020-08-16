from typing import List

"""
Problem Name: Longest Common Prefix

Problem Section: String

Problem Statement:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

Resources:

"""
""" 118 / 118 test cases passed.
	Status: Accepted
Runtime: 28 ms
Memory Usage: 14.2 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O()


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


myobj = Solution()
inpt = ["flower", "flow", "flight"]
print(myobj.longestCommonPrefix(inpt))
