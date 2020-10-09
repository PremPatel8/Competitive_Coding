from typing import List
from collections import defaultdict
from collections import Counter

"""
Problem Name: Minimum Window Substring

Problem Section: Arrays & Strings

Problem Statement:
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

Resources:
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/838/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
"""

""" 268 / 268 test cases passed.
	Status: Accepted
Runtime: 108 ms
Memory Usage: 14.5 MB """

# Solution techniques are Sliding Window Approach

# Time complexity : O(|S|+|T|) Space complexity : O(|S|+|T| . S)
""" Complexity Analysis
    Time Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T. In the worst case we might end up visiting every element of string S twice, once by left pointer and once by right pointer. ∣T∣ represents the length of string T.
    Space Complexity: O(∣S∣+∣T∣).∣S∣ when the window size is equal to the entire string S.∣T∣ when T has all unique characters. """


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)

        required = len(dict_t)

        l, r = 0, 0

        formed = 0

        window_counts = defaultdict(int)

        ans = float("inf"), None, None

        while r < len(s):

            character = s[r]
            window_counts[character] += 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


myobj = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(myobj.minWindow(S, T))
