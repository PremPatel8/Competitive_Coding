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


def findGrantsCap(grantsArray, newBudget):
    n = len(grantsArray)

    # sort the array in a descending order.
    grantsArray.sort(reverse=True)

    # pad the array with a zero at the end to
    # cover the case where 0 <= cap <= grantsArray[i]
    grantsArray.append(0)

    # calculate the total amount we need to
    # cut back to meet the reduced budget
    surplus = sum(grantsArray) - newBudget

    # if there is nothing to cut, simply return
    # the highest grant as the cap. Recall that
    # the grants array is sorted in a descending
    # order, so the highest grant is positioned
    # at index 0
    if (surplus <= 0):
        return grantsArray[0]

    # start subtracting from surplus the
    # differences (“deltas”) between consecutive
    # grants until surplus is less or equal to zero.
    # Basically, we are testing out, in order, each
    # of the grants as potential lower bound for
    # the cap. Once we find the first value that
    # brings us below zero we break

    i = 0
    for j in range(n-1):
        print(f"j = {j}")
        i = j
        surplus -= (j+1) * (grantsArray[j] - grantsArray[j+1])

        if (surplus <= 0):
            break

    # since grantsArray[i+1] is a lower bound
    # to our cap, i.e. grantsArray[i+1] <= cap,
    # we  need to add to grantsArray[i+1] the
    # difference: (-total / float(i+1), so the
    # returned value equals exactly to cap.
    return grantsArray[i+1] + (-surplus / float(i+1))


grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
res = findGrantsCap(grantsArray, newBudget)
print(f"{res} == 47 => {res == 47}")
