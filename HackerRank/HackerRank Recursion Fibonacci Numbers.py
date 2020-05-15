# # Unoptimized recursive solution
# def fibonacci(n):
#     if n >= 0 and n <=1:
#         return n
#     else:
#         return fibonacci(n-2)+fibonacci(n-1)

def fibonacci(n):
    # Using Memoization (Dynamic Programming) to reduce redundant calculations/function calls
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