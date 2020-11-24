"""
Time Complexity: sorting the grants array takes O(N⋅log(N)), calculating the surplus is O(N) due to the grants summation, 
and finally the for loop takes another O(N). In total, the time complexity is O(N⋅log(N)) before sorting and O(N) after sorting.
Space Complexity: throughout the algorithm we used only a constant amount of auxiliary space. The space complexity is therefore O(1).
"""


""" def find_grants_cap(grantsArray, newBudget):
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

        grantsAffectedSum += grant """


""" 
E.g:

  2+45, 2+45, 2+45, 2+45, 2, 0 - if 2+45 = 47 is cap
  2,  2,   2,   2,  2, 0 - if 2 was cap
 50,  50,  50,  50, 2, 0 - if 50 was cap
100,  100, 100, 50, 2, 0 - if 100 was cap
120,  120, 100, 50, 2, 0 - if 120 was cap
1000, 120, 100, 50, 2, 0 - Original grants array without 0

"""


def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort(reverse=True)

    grantsArray.append(0)

    grantsArrLen = len(grantsArray)

    surplus = sum(grantsArray) - newBudget

    if (surplus <= 0):
        return grantsArray[0]

    j = 0

    for i in range(grantsArrLen-1):
        # starting from grantsArray[i+1] that is considering value as index 1 as max cap
        # Take the delta with left value at index i
        # Multiply delta with the number of grants that will be affected by new cap which is i+1 and subtract this total amount from the surplus
        surplus -= (i+1) * (grantsArray[i] - grantsArray[i+1])

        if (surplus <= 0):
            # when the remaining surplus value becomes less than or equal to 0 we have found the index of the grant which is the lower bound of the cap value which is at i+1
            j = i
            break

    # the abs(surplus) is the amount of money left on the table, we divide it by the number of affected grants and add it to cap grant
    return grantsArray[j+1] + (abs(surplus) / float(j+1))


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
