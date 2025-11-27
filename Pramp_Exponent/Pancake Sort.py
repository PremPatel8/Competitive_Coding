import math


def pancake_sort(arr):
    def flip(arr, k):
        return arr[:k+1][::-1] + arr[k+1:]

    for i in range(len(arr)-1, 1, -1):
        maxIndex = arr.index(max(arr[:i+1]))
        arr = flip(arr, maxIndex)
        arr = flip(arr, i)

    return arr


inpt = [1, 5, 4, 3, 2]
print(pancake_sort(inpt))
