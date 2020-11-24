"""
Time Complexity: sorting the grants array takes O(N⋅log(N)), calculating the surplus is O(N) due to the grants summation, 
and finally the for loop takes another O(N). In total, the time complexity is O(N⋅log(N)) before sorting and O(N) after sorting.
Space Complexity: throughout the algorithm we used only a constant amount of auxiliary space. The space complexity is therefore O(1).
"""


def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort(reverse=True)
    grantsArray.append(0)
    grantsAffectedSum = 0

    surplus = sum(grantsArray)-newBudget

    # if surplus is less than or equal to 0 then we can directly use the largest grant value as cap
    if surplus <= 0:
        return grantsArray[0]

    # this variable will keep the running total of all the original grant values that will be affected by the temp new cap
    grantsAffectedSum += grantsArray[0]

    for i, grant in enumerate(grantsArray[1:], start=1):
        # this variable will have the total amount we reduce the affected grants by when we choose the current grant as the cap
        reductionAmtAffectedGrants = grantsAffectedSum - i*grant

        # the surplus amount left after subtracting the affected grants total reduction amount
        surplusLeft = surplus-reductionAmtAffectedGrants

        if surplusLeft <= 0:
            # the amount of money we are leaving on the table if we make the max cap as the current grant value
            moneyLeft = abs(surplusLeft)

            # we divide the money that is left by the number of affected grants and add it to the current grant which is the lower bound on the cap value
            return grant + (moneyLeft / float(i))

        grantsAffectedSum += grant


""" def find_grants_cap(grantsArray, newBudget):
    n = len(grantsArray)

    grantsArray.sort(reverse=True)

    grantsArray.append(0)

    surplus = sum(grantsArray) - newBudget

    if (surplus <= 0):
        return grantsArray[0]

    i = 0
    for j in range(n):
        i = j
        surplus -= (j+1) * (grantsArray[j] - grantsArray[j+1])

        if (surplus <= 0):
            break

    return grantsArray[i+1] + (-surplus / float(i+1)) """


# res = find_grants_cap(
#     [210, 200, 150, 193, 130, 110, 209, 342, 117], 1530)
# print(res)
# print(res == 211)


def test_find_grants_cap_1():
    assert find_grants_cap([2, 100, 50, 120, 1000], 190) == 47


def test_find_grants_cap_2():
    assert find_grants_cap([2, 4, 6], 3) == 1


def test_find_grants_cap_3():
    assert find_grants_cap([21, 100, 50, 120, 130, 110], 140) == 23.8


def test_find_grants_cap_4():
    assert find_grants_cap(
        [210, 200, 150, 193, 130, 110, 209, 342, 117], 1530) == 211


def test_find_grants_cap_5():
    assert find_grants_cap([2, 4], 3) == 1.5


def test_find_grants_cap_6():
    assert find_grants_cap([2, 100, 50, 120, 167], 400) == 128
