from typing import List
"""
Problem Name: Implement strStr()

Problem Section: String

Problem Statement:
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Constraints:
haystack and needle consist only of lowercase English characters.

Resources:

"""
""" 77 / 77 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 13.9 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or len(needle) == 0:
            return 0

        if len(haystack) < len(needle):  # early termination
            return -1

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


myobj = Solution()
haystack = "hello"
needle = "ll"
print(myobj.strStr(haystack, needle))
