""" Time Complexity: O(log(N))
Space Complexity: it’s O(1) """

""" To make sure we found the first element that satisfies arr[i] - i == 0, 
if in the binary search process we find an element that satisfies arr[i] - i == 0, we proceed to check if its the first element in the array, 
or that the element before it does not satisfy the condition. 
If not - we continue with the binary search, since this is not the first element that satisfies the condition. """


def index_equals_value_search(arr):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid_i = (left+right) // 2

        if arr[mid_i] - mid_i < 0:
            left = mid_i+1
        elif (arr[mid_i] - mid_i) == 0 and (mid_i == 0 or (arr[mid_i-1] - (mid_i-1)) < 0):
            return mid_i
        else:
            right = mid_i-1

    return -1


inpt = [-5, 0, 3, 4, 10, 18, 27]  # diffArr - [-5, -1, 1, 1, 6, 13, 21]
# the diff between arr[i] and i, that is arr[i] - i is a monotonically increasing sequence, which means Binary search can be applied on it
# inpt =  [0, 3], diffArr - [0, 2]
# inpt = [-8, 0, 2, 5], diffArr - [-8, -1, 0, 2]
# inpt = [-5, 0, 2, 3, 10, 29]  # diffArr - [-5, -1, 0, 0, 6, 24]
print(index_equals_value_search(inpt))
