"""
Bracket Match

A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Examples:

input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2

Constraints:

    [time limit] 5000ms

    [input] string text
        1 ≤ text.length ≤ 5000

    [output] integer
"""
""" 
Time Complexity - O(n)
Space Complexity - O(n)
"""


def bracket_match(text):
    stack = []
    res = 0
    op_brackets = {"(": ")"}

    for bracket in text:
        if bracket in op_brackets:
            stack.append(bracket)
        else:
            if stack:
                stack_top = stack.pop()
                if op_brackets[stack_top] != bracket:
                    res += 1
            else:
                res += 1

    res += len(stack)
    return res


inpt = "(()"
# expected output = 1
print(bracket_match(inpt))
