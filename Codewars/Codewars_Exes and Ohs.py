def xo(s):
    print(s)
    count = 0
    
    for c in s:
        if c.lower() == 'x':
            count += 1
        elif c.lower() == 'o':
            count -= 1
    
    print(count)
    
    if count == 0:
        return True
    else:
        return False
        
print(xo('xxxoo'))