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


# inpt = "())("
inpt = ")"
print(bracket_match(inpt))
