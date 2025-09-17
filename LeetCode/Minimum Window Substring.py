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

        str_t_char_freq_dict = Counter(t)

        required_substr_chars_len = len(str_t_char_freq_dict)

        left = 0
        right = 0
        
        # keep track of how many unique characters in t are present in the current window in its desired frequency,
        # so it will only be incremented when the char is in t and it's freq so far is equal to it's freq in string t
        formed = 0

        # keeps a count of all the unique characters in the current window
        window_char_freq_dict = defaultdict(int)

        # ans tuple of the form (window length, left, right)
        ans = (float("inf"), None, None)

        while right < len(s):
            # Add one character from the right to the window
            currChr = s[right]
            window_char_freq_dict[currChr] += 1

            # If the current char is in string t and it's frequency added up so far equals to the desired count in t then increment the formed count by 1.
            if currChr in str_t_char_freq_dict and window_char_freq_dict[currChr] == str_t_char_freq_dict[currChr]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable' OR left pointer has reached the same position as right pointer
            while left <= right and formed == required_substr_chars_len:
                currChr = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Decreases frequency count of the leftmost character as we're about to move the left pointer
                window_char_freq_dict[currChr] -= 1
                
                # Check if window becomes invalid, AKA this currChr is in the string t and removing it means the current window does not have all the characters from string t
                if currChr in str_t_char_freq_dict and window_char_freq_dict[currChr] < str_t_char_freq_dict[currChr]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
    
    
    from collections import Counter, defaultdict

    # Filtered String Optimization AND Early Termination Check solution
    def minWindow_filtered_string_optimization(self, s: str, t: str) -> str:
        # Early termination checks
        if not t or not s or len(s) < len(t):
            return ""
        
        # Quick check: if s doesn't contain all unique chars from t
        s_chars = set(s)
        if not all(char in s_chars for char in set(t)):
            return ""
        
        str_t_char_freq_dict = Counter(t)
        required_substr_chars_len = len(str_t_char_freq_dict)
        
        # Filtered String Optimization: Only consider characters that appear in t
        filtered_s = []
        for i, char in enumerate(s):
            if char in str_t_char_freq_dict:
                filtered_s.append((i, char))  # (original_index, character)
        
        # If no characters from t found in s (shouldn't happen due to early check, but safety)
        if not filtered_s:
            return ""
        
        left = 0
        right = 0
        formed = 0
        window_char_freq_dict = defaultdict(int)
        ans = (float("inf"), None, None)
        
        while right < len(filtered_s):
            # Get character from filtered string
            currChr = filtered_s[right][1]
            window_char_freq_dict[currChr] += 1
            
            if currChr in str_t_char_freq_dict and window_char_freq_dict[currChr] == str_t_char_freq_dict[currChr]:
                formed += 1
            
            # Try to contract the window from left
            while left <= right and formed == required_substr_chars_len:
                currChr = filtered_s[left][1]
                
                # Calculate window size using original indices from s
                original_left = filtered_s[left][0]
                original_right = filtered_s[right][0]
                window_size = original_right - original_left + 1
                
                if window_size < ans[0]:
                    ans = (window_size, original_left, original_right)
                
                window_char_freq_dict[currChr] -= 1
                if currChr in str_t_char_freq_dict and window_char_freq_dict[currChr] < str_t_char_freq_dict[currChr]:
                    formed -= 1
                left += 1
            
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


myobj = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(myobj.minWindow(S, T))
