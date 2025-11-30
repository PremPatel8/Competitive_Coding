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

class Solution:
    # Backtracking solution
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            for letter in letters[digits[index]]:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        
        return combinations
    
    
    # Iterative BFS sol, higher space usage and not as intuitive
    def letterCombinations(self, digits: str) -> List[str]:
        output = deque()
        
        if not len(digits):
            return list(output)

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

        return list(output)


myobj = Solution()

print(myobj.letterCombinations("23"))