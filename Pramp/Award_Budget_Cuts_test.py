def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort(reverse=True)
    grantsArray.append(0)
    grantsArrSum = sum(grantsArray)
    # grantsArrayLen = len(grantsArray)
    grantsAffectedSum = 0

    surplus = grantsArrSum-newBudget

    if surplus <= 0:
        return grantsArray[0]

    grantsAffectedSum += grantsArray[0]

    for i, grant in enumerate(grantsArray[1:], start=1):
        newGrantsSum = grantsAffectedSum - i*grant

        updatedSumDelta = grantsArrSum-newGrantsSum

        if updatedSumDelta - newBudget <= 0:
            diff = newBudget-updatedSumDelta

            return grant + (abs(diff) / float(i))

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
