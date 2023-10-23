from typing import List
from collections import deque

"""
Problem Name: Valid Parentheses

Problem Section: Others / Bit Manipulation

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example:
Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Resources:

"""

""" 91 / 91 test cases passed.
	Status: Accepted
Runtime: 24 ms
Memory Usage: 14 MB """

# Solution techniques are
# Time complexity : O(n) Space complexity : O(n) My solution using Queue


class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = deque()
        pairs_dict = {'(': ')', '[': ']', '{': '}'}

        for para in s:
            if para in pairs_dict:
                p_stack.append(para)
            else:
                if p_stack:
                    left_p = p_stack.pop()

                    if pairs_dict[left_p] != para:
                        return False
                else:
                    return False

        return True if len(p_stack) == 0 else False


# My Python Stack (Deque) and Dict sol with fewer lines of code
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pair = {'(':')', '{':'}','[':']'}
        stack = deque()
        
        for curr_bracket in s:
            # If curr_bracket is a opening bracket
            if curr_bracket in bracket_pair:
                stack.append(curr_bracket)
            # If curr_bracket is a closing bracket
            elif len(stack) == 0 or bracket_pair[stack.pop()] != curr_bracket:
                return False
        
        return len(stack) == 0
    

# My Java Stack and HashMap solution with fewer lives of code
class Solution {
    public boolean isValid(String s) {
     Stack<Character> stack = new Stack<>();
     HashMap<Character, Character> bracketPair = new HashMap<>();
     bracketPair.put('(', ')');
     bracketPair.put('{', '}');
     bracketPair.put('[', ']');

     for (char currBracket : s.toCharArray()) {
         // currBracket a opening bracket
         if (bracketPair.containsKey(currBracket)) {
             stack.push(currBracket);
         } else if (stack.size() <= 0 || !bracketPair.get(stack.pop()).equals(currBracket)) {
             // currBracket a closing bracket
             return false;
         }
     }

     return stack.size() == 0;
    }
}

myobj = Solution()
# s = "()[]{}"
# s = "([)]"
# s = "{[]}"
s = '['
print(myobj.isValid(s))
