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
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/discuss/503450/JavaPython-3-Count-occurrences-and-sum-the-difference-w-analysis.
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/discuss/503535/Python-3-(two-lines)-(beats-100)

runtime: 
63 / 63 test cases passed.
	Status: Accepted
Runtime: 112 ms
Memory Usage: 14.8 MB

"""

# Solution techniques are

# Time complexity : O() Space complexity : O()


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = collections.Counter(s)
        t_freq = collections.Counter(t)
        freq_diff = s_freq - t_freq

        return sum(max(0, freq_diff[s_chr]) for s_chr in s_freq)


myobj = Solution()
s = "bab"
t = "aba"
print(myobj.minSteps(s, t))
