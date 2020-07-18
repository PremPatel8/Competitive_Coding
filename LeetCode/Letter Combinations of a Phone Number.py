from typing import List
from collections import deque

"""
Problem Name: Letter Combinations of a Phone Number

Problem Section: Backtracking

Probelm Statement: 
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

1:None, 2:a,b,c, 3:d,e,f
4:g,h,i, 5:j,k,l, 6:m,n,o
7:p,q,r,s, 8:t,u,v, 9:w,x,y,z

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

# Nick White Solution, Queue based approach


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = deque()
        if not len(digits):
            return output

        output.append("")

        char_map = ['0', '1', "abc", "def", "ghi",
                    "jkl", "mno", "pqrs", "tuv", "wxyz"]

        i = 0

        while(i < len(digits)):
            index = int(digits[i])

            while len(output[0]) == i:
                permutation = output.popleft()

                for ch in char_map[index]:
                    output.append(permutation+ch)

            i += 1

        return output


myobj = Solution()

print(myobj.letterCombinations("23"))

#%%
digit = "3"
digit[1:]
