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
    Time Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T. 
    In the worst case we might end up visiting every element of string S twice, once by left pointer and once by right pointer.
    Creating t_char_freq using Counter(t): O(|T|)
    
    Space Complexity: O(∣S∣+∣T∣).∣S∣ when the window size is equal to the entire string S.∣T∣ when T has all unique characters.
    t_char_freq: Stores at most all unique characters from t → O(|T|)
    In practice, this is bounded by O(1) if we assume a fixed character set (e.g., 52 letters for uppercase/lowercase, or 128 for ASCII).
    window_char_freq: Stores at most all unique characters from s → O(|S|)
    Similarly bounded by O(1) for fixed character sets
    """


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Early termination checks
        if not t or not s or len(s) < len(t):
            return ""

        t_char_freq = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        # Since we only increment formed when the character AND it's freq match its value in string t,
        # hence here we count only the unique chars of t as required chars
        required_window_chars = len(t_char_freq)

        # keep track of how many unique characters in t are present in the current window in its desired frequency,
        # so it will only be incremented when the char is in t and it's freq so far is equal to it's freq in string t
        found_window_chars = 0

        # keeps a count of all the unique characters in the current window
        window_char_freq = defaultdict(int)

        result = [-1, -1]
        min_window_len = float("inf")

        left = 0

        for right in range(len(s)):
            curr_right_char = s[right]
            window_char_freq[curr_right_char] += 1

            # If the current char is in string t and it's frequency added up so far equals to the desired count in t,
            # then increment the found_window_chars count by 1.
            if curr_right_char in t_char_freq and window_char_freq[curr_right_char] == t_char_freq[curr_right_char]:
                found_window_chars += 1
            
             # Try and contract the window till the point where it ceases to be desirable 
             # OR left pointer has reached the same position as right pointer
            while left <= right and found_window_chars == required_window_chars:
                curr_left_Chr = s[left]
                curr_window_len = right - left + 1

                if curr_window_len < min_window_len:
                    result = [left, right]
                    min_window_len = curr_window_len

                # Decreases frequency count of the leftmost character as we're about to move the left pointer
                window_char_freq[curr_left_Chr] -= 1
                
                # Check if window becomes invalid, AKA this curr_left_Chr is in the string t 
                # and removing it means the current window does not have all the characters from string t
                if curr_left_Chr in t_char_freq and window_char_freq[curr_left_Chr] < t_char_freq[curr_left_Chr]:
                    found_window_chars -= 1

                left += 1
        
        l, r = result

        return s[l : r + 1] if min_window_len != float("inf") else ""
    
    
    """
    The key optimization in this approach is the filtered_s list: where filtered_S is the string formed from S by removing all the elements not present in T.
    
    This complexity reduction is evident when ∣filtered_S∣<<<∣S∣.

    Best case scenario: If t contains rare characters and s is very large but has few matches, filtered_s becomes much smaller than s.

    Trade-off: This solution uses extra O(|S|) space for filtered_s, but can be faster in practice when there are many characters in s that aren't in t

    This optimization is particularly effective when t is small and contains characters that appear infrequently in s.
    """

    # Filtered String Optimization AND Early Termination Check solution
    def minWindow_filtered_string_optimization(self, s: str, t: str) -> str:
        # Early termination checks
        if not t or not s or len(s) < len(t):
            return ""

        t_char_freq = Counter(t)
        required_window_chars = len(t_char_freq)

        found_window_chars = 0
        
        window_char_freq = defaultdict(int)

        result = [-1, -1]
        min_window_len = float("inf")

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in t_char_freq:
                filtered_s.append((i, char))
        
        # If no characters from t is found in s
        if not filtered_s:
            return ""

        left = 0
        for right in range(len(filtered_s)):
            curr_right_char = filtered_s[right][1]
            window_char_freq[curr_right_char] += 1

            if window_char_freq[curr_right_char] == t_char_freq[curr_right_char]:
                found_window_chars += 1
            
            while left <= right and found_window_chars == required_window_chars:
                curr_left_Chr = filtered_s[left][1]
                left_idx = filtered_s[left][0]
                right_idx = filtered_s[right][0]
                curr_window_len = right_idx - left_idx + 1

                if curr_window_len < min_window_len:
                    result = [left_idx, right_idx]
                    min_window_len = curr_window_len
                    
                window_char_freq[curr_left_Chr] -= 1
                
                if window_char_freq[curr_left_Chr] < t_char_freq[curr_left_Chr]:
                    found_window_chars -= 1

                left += 1
        
        l, r = result

        return s[l : r + 1] if min_window_len != float("inf") else ""


myobj = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(myobj.minWindow(S, T))
