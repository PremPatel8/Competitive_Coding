# My Time O(N) Space O(N) solution using set
""" def get_different_number(arr):
    arrSet = set(arr)
    arrLen = len(arr)

    for i in range(0, arrLen):
        if i not in arrSet:
            return i

    return arrLen """

# Time O(N), Space O(1) optimized sol


def get_different_number(arr):
    arrLen = len(arr)

    for i in range(arrLen):
        temp = arr[i]

        while temp < arrLen and arr[temp] != temp:
            arr[temp], temp = temp, arr[temp]
            # Fails:
            # temp, arr[temp] = arr[temp], temp

    for i in range(arrLen):
        if arr[i] != i:
            return i

    return arrLen


def test_get_different_number():
    assert get_different_number([0, 1, 2, 3]) == 4


def test_get_different_number_1():
    assert get_different_number([0, 99999, 100000]) == 1


def test_get_different_number_2():
    assert get_different_number([0]) == 1


def test_get_different_number_3():
    assert get_different_number([0, 1, 2]) == 3


def test_get_different_number_4():
    assert get_different_number([1, 3, 0, 2]) == 4


def test_get_different_number_5():
    assert get_different_number([100000]) == 0


def test_get_different_number_6():
    assert get_different_number([1, 0, 3, 4, 5]) == 2


def test_get_different_number_7():
    assert get_different_number([0, 100000]) == 1


def test_get_different_number_8():
    assert get_different_number([0, 5, 4, 1, 3, 6, 2]) == 7
