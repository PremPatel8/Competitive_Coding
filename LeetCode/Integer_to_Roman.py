from typing import DefaultDict, List
import bisect

"""
Problem Name: Integer to Roman

Problem URL: https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2964/

Problem Section: 

Problem Statement:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.
 

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:
1 <= num <= 3999


Resources:


"""

# My solution

# Time complexity : O(n) Space complexity : O(n)

""" 3999 / 3999 test cases passed.
	Status: Accepted
Runtime: 60 ms
Memory Usage: 14.3 MB """

class Solution:
    # def find_le(self, a, x):
    #     'Find rightmost value less than or equal to x'
    #     i = bisect.bisect_right(a, x)
    #     if i:
    #         return a[i-1]
    #     raise ValueError

    # def find_ge(self, a, x):
    #     'Find leftmost item greater than or equal to x'
    #     i = bisect.bisect_left(a, x)
    #     if i != len(a):
    #         return a[i]
    #     raise ValueError

    def nextSmallest(self, keys, num):
        for no in keys:
            if no <= num:
                return no

    def intToRoman(self, num: int) -> str:
        intToRomanDict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                          90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        res = ""

        keys = sorted([int(x) for x in intToRomanDict.keys()], reverse=True)

        # print(keys)

        while num:
            nextSmallestNum = self.nextSmallest(keys, num)
            res += intToRomanDict[nextSmallestNum]
            num -= nextSmallestNum

        return res


# myobj = Solution()
# inpt = 58
# inpt = 3
# inpt = 4
# inpt = 9
# inpt = 1994
# print(myobj.intToRoman(inpt))
