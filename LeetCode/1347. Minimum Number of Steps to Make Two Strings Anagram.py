from typing import List
import collections

"""
Problem Name: 1347. Minimum Number of Steps to Make Two Strings Anagram

Problem URL: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

Problem Section: String

Problem Statement:
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Constraints:

    1 <= s.length <= 50000
    s.length == t.length
    s and t contain lower-case English letters only.


Resources:

runtime: 

"""

# Solution techniques are

# Time complexity : O() Space complexity : O()


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0

        freq_count_s = collections.Counter(s)

        for ch in t:
            if freq_count_s[ch] > 0:
                freq_count_s[ch] -= 1
            else:
                res += 1

        return res


myobj = Solution()
s = "bab"
t = "aba"
print(myobj.minSteps(s, t))
