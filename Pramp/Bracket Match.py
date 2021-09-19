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
""" Space optimized solution
Time Complexity - O(n)
Space Complexity - O(1)

Notice that a string of matching brackets is a string that follows these rules:
the number of '(' and the number of ')' are equal i.e. every open bracket is matched with a closing bracket.
There cannot be a closing bracket before an opening bracket, i.e. in every prefix of the string, the number of '(' is equal or greater than the number of ')'.

To check how many brackets we need to add an existing string, we need to keep track of the number of '(' and the number of ')', or more accurately the difference between the number of '(' and the number of ')'. We iterate through the string, and count the difference between the open and close brackets, if at some point there are more ')' than '(' [i.e. diffCount < 0], it means that to fix the string, we must add an '(' somewhere before the current position (for example, the beginning of the string). Thus, in our algorithm we’ll add 1 to the answer and also increment the number of '(' by one in our difference counter. This promises the second rule is correct in our string.

To make sure the first rule is correct, we simply take the difference between the '(' and the ')' in the text, and add it to the answer, since at the end of the string if the number isn’t equal, we’ll simply add ')' to the end of the text (or '(' to the beginning).
"""


""" def bracket_match(text):
    diffCount = 0
    res = 0

    for i in range(len(text)):
        currBrac = text[i]

        if currBrac == "(":
            diffCount += 1
        elif currBrac == ")":
            diffCount -= 1

        if diffCount < 0:
            diffCount += 1
            res += 1

    res += diffCount
    return res """


# My Alt solution, with early termination of the for loop
def bracket_match(text):
    bracket_pair = {'(': ')'}
    opening_brackets = []
    res = 0

    for idx, bracket in enumerate(text):
        if bracket in bracket_pair:
            opening_brackets.append(bracket)
        else:
            if len(opening_brackets) == 0:
                res = len(text)-idx
                break
            else:
                opening_brackets.pop()

    if len(opening_brackets) != 0:
        res = len(opening_brackets)

    return res


inpt = "(()"
# expected output = 1
print(bracket_match(inpt))
