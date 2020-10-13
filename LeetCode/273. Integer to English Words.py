from typing import List

"""
Problem Name: 273. Integer to English Words

Problem URL: https://leetcode.com/problems/integer-to-english-words/

Problem Section: Strings, Numbers, Math

Problem Statement:
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"



Resources:

runtime: 
601 / 601 test cases passed.
	Status: Accepted
Runtime: 32 ms
Memory Usage: 14.3 MB

positive integer less than 2**31-1 MAX - 2,147,483,646 (
two billion one hundred forty-seven million four hundred eighty-three thousand six hundred forty-six)
0 <= num < 2**31-1

Billion -
100 Million -
10 Million -
1 Million -
100 Thousand -
10 Thousand -
1 Thousand -
Hundreds -
Tens -
Units - cases - 0 - ignore towards next digit
                1 - 
"""

# Solution techniques are

# Time complexity : O(n) Space complexity : O(n)


class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n % 10)
            if n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + words(n % 100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n % 1000**p)

        return ' '.join(words(num)) or 'Zero'


myobj = Solution()
inpt = 12345
print(myobj.numberToWords(inpt))

# Alt syntax
""" def __init__(self):
    self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    self.thousands = ["","Thousand","Million","Billion"]

def numberToWords(self, num):
    if num == 0:
        return "Zero"
    res = ""
    for i in range(len(self.thousands)):
        if num % 1000 != 0:
            res = self.helper(num%1000) + self.thousands[i] + " " + res
        num /= 1000
    return res.strip()

def helper(self, num):
    if num == 0:
        return ""
    elif num < 20:
        return self.lessThan20[num] + " "
    elif num < 100:
        return self.tens[num/10] + " " + self.helper(num%10)
    else:
        return self.lessThan20[num/100] + " Hundred " + self.helper(num%100) """