import math

"""
b = 190
G = [2, 100, 50, 120, 1000]
[2, 47, 47, 47, 47]
c = 47

time: O(log b * |G|)
space: O(1)
"""


""" def find_grants_cap(G, b):
    def comp_total(c): return sum(min(c, g) for g in G)
    l, r = 0, b
    while l < r:
        m = (l + r) / 2
        total = comp_total(m)
        if abs(total - b) < 0.0001:
            return m
        else:
            l, r = ((m, r), (l, m))[total > b] """


def find_grants_cap(grantsArray, newBudget):
    noGrants = len(grantsArray)
    avgGrant = newBudget / noGrants

    noAffected = 0
    sumUnaffected = 0

    for grant in grantsArray:
        if grant <= avgGrant:
            sumUnaffected += grant
        elif grant > avgGrant:
            noAffected += 1

    newCap = (newBudget-sumUnaffected) / noAffected

    return newCap


def test_find_grants_cap():
    # Pass
    assert find_grants_cap([2, 100, 50, 120, 1000], 190) == 47
    assert find_grants_cap([2, 4], 3) == 1.5
    assert find_grants_cap([2, 4, 6], 3) == 1
    assert find_grants_cap([21, 100, 50, 120, 130, 110], 140) == 23.8
    # Fail
    assert find_grants_cap(
        [210, 200, 150, 193, 130, 110, 209, 342, 117], 1530) == 211
