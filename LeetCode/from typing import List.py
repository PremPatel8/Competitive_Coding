from typing import List
from collections import Counter
"""
Problem Name: Count and Say

Problem Section: String

Problem Statement:
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, 
in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

Example 2:
Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, 
the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".

Resources:

"""
""" 18 / 18 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14 MB """

# Solution techniques are
# Time complexity : O() Space complexity : O() My solution using DP and string iteration to get digit freq counts


class Solution:
    def countAndSay(self, n: int) -> str:
        dp = [""]*n
        dp[0] = "1"

        def encode(val):
            newVal = ""
            numFreq = []
            i = 0

            while i < len(val):
                currVal = val[i]
                count = 0
                while i < len(val) and val[i] == currVal:
                    count += 1
                    i += 1

                numFreq.append((count, currVal))

            for count, num in numFreq:
                # print(key)
                newVal += str(count)
                newVal += num

            return newVal

        for i in range(1, n):
            dp[i] = encode(dp[i-1])

        return dp[n-1]


myobj = Solution()
inpt = 8
print(myobj.countAndSay(inpt))
