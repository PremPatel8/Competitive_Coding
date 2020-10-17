import math

"""
b = 190
G = [2, 100, 50, 120, 1000]
[2, 47, 47, 47, 47]
c = 47

time: O(log b * |G|)
space: O(1)
"""


def find_grants_cap(G, b):
    def comp_total(c): return sum(min(c, g) for g in G)
    l, r = 0, b
    while l < r:
        m = (l + r) / 2
        total = comp_total(m)
        if abs(total - b) < 0.0001:
            return m
        else:
            l, r = ((m, r), (l, m))[total > b]

#print(find_grants_cap([2, 100, 50, 120, 1000], 190))


grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
print(math.ceil(find_grants_cap(grantsArray, newBudget)))
print(f"{find_grants_cap(grantsArray, newBudget)} == 47 => {math.ceil(find_grants_cap(grantsArray, newBudget)) == 47}")
