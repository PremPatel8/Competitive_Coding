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
Runtime: 28 ms
Memory Usage: 14.3 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() My optimized solution using string translation to remove punctuations and convert to lowercase and iterating from both sides to compare values


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lowercase = s.lower()
        combined_str = s_lowercase.translate(str.maketrans('', '', string.punctuation+string.whitespace))

        len_combined = len(combined_str)

        for i in range(len_combined//2):
            if combined_str[i] != combined_str[len_combined-i-1]:
                return False

        return True


myobj = Solution()
inpt = "A man, a plan, a canal: Panama"
# inpt = "race a car"
print(myobj.isPalindrome(inpt))


""" 
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True
 """