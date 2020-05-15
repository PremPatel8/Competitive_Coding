def fibonacci(n):
    mem = {}
    
    if n in mem:
        return mem[n]
    if n <= 1:
        return n
    else:
        v = fibonacci(n-1) + fibonacci(n-2)
        mem[n] = v
        return v

n = int(input())
print(fibonacci(n))