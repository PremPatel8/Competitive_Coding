def accum(s):
    ans = ""
    for i, c in enumerate(s):
        ans += c.upper()

        for _ in range(i):
            ans += c.lower()
        
        if i != len(s)-1:
            ans += '-'
    
    return ans