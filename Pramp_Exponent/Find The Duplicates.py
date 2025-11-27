"""
Find The Duplicates

Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2

Constraints:

    [time limit] 5000ms

    [input] array.integer arr1
        1 ≤ arr1.length ≤ 100

    [input] array.integer arr2
        1 ≤ arr2.length ≤ 100

    [output] array.integer
"""
# Time complexity: O(n log m), space O(1)

def find_duplicates(arr1, arr2):
    arr1Len = len(arr1)
    arr2Len = len(arr2)
    output = []

    biggerArr, smallerArr = (arr1, arr2) if arr1Len > arr2Len else (arr2, arr1)

    def presentInBiggerArr(num):
        left = 0
        right = len(biggerArr)-1

        while left <= right:
            mid = (left+right) // 2

            if biggerArr[mid] < num:
                left = mid+1
            elif biggerArr[mid] > num:
                right = mid-1
            else:
                return True

        return False

    for num in smallerArr:
        if presentInBiggerArr(num):
            output.append(num)

    return output


arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates(arr1, arr2))
