# My Time O(N) Space O(N) solution using set
""" def get_different_number(arr):
    arrSet = set(arr)
    arrLen = len(arr)

    for i in range(0, arrLen):
        if i not in arrSet:
            return i

    return arrLen """

# Time O(N) Space O(N) Alt Set based solutin


""" def get_different_number(arr):
    seen = set(arr)

    for no in range(2*31-1):
        if no not in seen:
            return no """

# Time O(N), Space O(1) optimized sol


def get_different_number(arr):
    arrLen = len(arr)

    for i in range(arrLen):
        temp = arr[i]

        while temp < arrLen and arr[temp] != temp:
            next_index = arr[temp]
            arr[temp] = temp
            temp = next_index

    for i in range(arrLen):
        if arr[i] != i:
            return i

    return arrLen
