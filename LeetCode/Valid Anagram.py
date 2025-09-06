from typing import List
from collections import Counter
"""
Problem Name: Valid Anagram

Problem Section: String

Problem Statement:
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Resources:
"""


# Solution techniques are
# Time complexity : O() Space complexity : O() solution using string sorting


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return len(Counter(s)-Counter(t)) == 0


# myobj = Solution()
# s = "anagram"
# t = "nagaram"
# # s = "a"
# # t = "ab"
# print(myobj.isAnagram(s, t))






"Java"

""" 
Time complexity : O(n)
Space complexity : O(1)
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false;
    }
    int[] counter = new int[26];
    for (int i = 0; i < s.length(); i++) {
        counter[s.charAt(i) - 'a']++;
        counter[t.charAt(i) - 'a']--;
    }
    for (int count : counter) {
        if (count != 0) {
            return false;
        }
    }
    return true;
}
 """
