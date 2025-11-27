""" 1: 4, 2 - 2
2: 27, 3 - 3
3: 16, 4 - 2
4: 3, 2 - 1.732
5: 10, 3 - 2.154
6: 160, 3 - 5.429 """

# Binary Search approach
# Time Complexity - O(log x), Space Complexity - O(1)


def root(x, n):
    if x*n == 0:
        return 0

    lowerBound = 0
    upperBound = max(1, x)

    approxRoot = float(upperBound + lowerBound) / 2

    while (approxRoot - lowerBound >= 0.001):
        if (pow(approxRoot, n) > x):
            upperBound = approxRoot
        elif (pow(approxRoot, n) < x):
            lowerBound = approxRoot
        else:
            break

        approxRoot = (upperBound + lowerBound) / 2

    return approxRoot


""" def root1(a, n):
    if a * n == 0:
        return 0
    x0, x1 = a, 0
    while x0 > a / (x0 ** (n - 1)):  # prevent overflow
        x1 = x0 - (x0 ** n - a) / (n * x0 ** (n - 1))
        if x0 == x1:
            break
        x0 = x1
    return x0 """


# print(root(7, 3))
print(root(3, 2))
