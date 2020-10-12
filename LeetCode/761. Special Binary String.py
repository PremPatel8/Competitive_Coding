from typing import List

"""
Problem Name: 761. Special Binary String

Problem Section: String, Recursion

Problem Statement:
 Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.

Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

Example 1:

Input: S = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

Note:

    S has length at most 50.
    S is guaranteed to be a special binary string as defined above.


Resources:
https://leetcode.com/problems/special-binary-string/discuss/581356/Thorough-explanation-using-Validate-Parentheses-based-on-others'-solutions
"""

""" runtime """

# Solution techniques are

# Time complexity : O() Space complexity : O()


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        i = 0  # start of the substring
        count = 0  # to find a valid substring by counting 1's and 0's
        res = []  # store the transformed substrings
        for j, v in enumerate(S):
            # j would be the end of the substring
            # v is the current character being checked
            if v == "1":
                count += 1
            else:
                count -= 1
            # add to count when seeing 1, reduce count when seeing 0
            # when count is 0 again, means we just parsed a valid substring
            if count == 0:
                # take the inside of the substring, transform it using recursion
                # and add to the set of completed results
                res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                # move the start of the substring to the next character
                i = j + 1
        res.sort()  # make sure the substrings are ordered from lexigraphically smallest to largest
        res = res[::-1]  # now it's largest to smallest
        # join and return
        return ''.join(res)


myobj = Solution()
inpt = "11011000"
print(myobj.makeLargestSpecial(inpt))
