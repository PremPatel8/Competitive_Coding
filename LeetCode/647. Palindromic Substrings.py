from typing import List

"""
Problem Name: 647. Palindromic Substrings

Problem URL: https://leetcode.com/problems/palindromic-substrings/

Problem Section: String

Problem Statement:
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Resources:

runtime:
130 / 130 test cases passed.
	Status: Accepted
Runtime: 112 ms
Memory Usage: 14 MB 

"""

# Solution techniques are generate a list of center indexes and left and right index for each center, 
# keep expanding leaft and right index so long as the chars at those indexes match and the indexs are within the bound 0 and len(string)

# Time complexity : O(n**2) Space complexity : O(1)


class Solution:
    def countSubstrings(self, s: str) -> int:
        slen = len(s)
        res = 0

        for center in range(2*slen-1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < slen and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res


myobj = Solution()
inpt = "aaa"
print(myobj.countSubstrings(inpt))
