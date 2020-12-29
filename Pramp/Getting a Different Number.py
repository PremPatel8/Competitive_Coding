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
            temp, arr[temp] = arr[temp], temp

    for i in range(arrLen):
        if arr[i] != i:
            return i

    return arrLen


def test_get_different_number():
    arr = [0, 1, 2, 3]
    output = 4
    assert get_different_number(arr) == output
