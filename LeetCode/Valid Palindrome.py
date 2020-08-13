from typing import List
import string
"""
Problem Name: Valid Palindrome

Problem Section: String

Problem Statement:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false 

Constraints:
s consists only of printable ASCII characters.

Resources:
"""
""" 481 / 481 test cases passed.
	Status: Accepted
Runtime: 36 ms
Memory Usage: 15.1 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() My solution using string translation to remove punctuations and convert to lowercase and iterating from both sides to compare values


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lowercase = s.lower()
        s_lowercase = s_lowercase.translate(str.maketrans('', '', string.punctuation))
        # print(s_lowercase)

        combined_str = "".join(s_lowercase.split())
        # print(combined_str)

        len_combined = len(combined_str)

        for i in range(len_combined//2):
            if combined_str[i] != combined_str[len_combined-i-1]:
                return False

        return True


myobj = Solution()
# inpt = "A man, a plan, a canal: Panama"
inpt = "race a car"
print(myobj.isPalindrome(inpt))
