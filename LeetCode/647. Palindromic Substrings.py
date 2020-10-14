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
# Alt solution using DP

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

    # def countSubstrings(self, s: str) -> int:
	#     L, r = len(s), 0
	#     for i in range(L):
	#     	for a,b in [(i,i),(i,i+1)]:
	#     		while a >= 0 and b < L and s[a] == s[b]: a -= 1; b += 1
	#     		r += (b-a)//2
	#     return r

    """ DP Solution """
    # def countSubstrings(self, s):
    # if not s:
    #     return 0

    # n = len(s)
    # table = [[False for x in range(n)] for y in range(n)]
    # count = 0

    # # Every isolated char is a palindrome
    # for i in range(n):
    #     table[i][i] = True
    #     count += 1

    # # Check for a window of size 2
    # for i in range(n-1):
    #     if s[i] == s[i+1]:
    #         table[i][i+1] = True
    #         count += 1

    # # Check windows of size 3 and more
    # for k in range(3, n+1):
    #     for i in range(n-k+1):
    #         j = i+k-1
    #         if table[i+1][j-1] and s[i] == s[j]:
    #             table[i][j] = True
    #             count += 1

    # return count


myobj = Solution()
inpt = "aaa"
print(myobj.countSubstrings(inpt))
