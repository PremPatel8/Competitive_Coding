def is_isogram(string):
    charSet = set()
    
    if string:
        return True
    
    for c in string:
        chr = c.lower()
        if charSet and chr in charSet:
            return False
        else:
            charSet.add(chr)

print(is_isogram("aba"))