""" A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

For example,

[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]

is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]

isn’t a Toeplitz matrix, so we should return false.

Constraints:

    [time limit] 5000ms
    [input] array.array.integer arr
        0 ≤ arr.length ≤ 20
        0 ≤ arr[i].length ≤ 20
        0 ≤ arr[i][j] ≤ 20
    [output] boolean
 """

# Optimized Dict Sol
"""
Time Complexity : O(RC)
Space Complexity : O(N) - N is no of unique elements in matrix

   0  1  2  3
0 [1, 2, 3, 4]
1 [5, 1, 2, 3]
2 [6, 5, 1, 2]

1 : (0,0), (1,1), (2,2) - diff between Col and Row (Col-Row) == 0 for every index
2 : (0,1), (1,2), (2,3) - diff between Col and Row (Col-Row) == 1 for every index
3 : (0,2), (1,3)

4 : (0,3)

5 : (1,0), (2,1) - diff between Col and Row (Col-Row) == -1 for every index

6 : (2,0)
"""


def isToeplitz(arr):
    rows = len(arr)
    cols = len(arr[0])

    if not rows or rows == 1 or not cols or cols == 1:
        return True

    seen_dict = {}

    for row in range(rows):
        for col in range(cols):
            curr_ele = arr[row][col]

            if curr_ele in seen_dict:
                if seen_dict[curr_ele] != (col-row):
                    return False
            else:
                seen_dict[curr_ele] = col-row

    return True


# My sol using List Silicing
"""
K = No of cols - 1
Time Complexity : O(K + R*K) ~ O(RK)
Space Complexity : O(K)
"""

""" def isToeplitz(arr):
    rows = len(arr)
    cols = len(arr[0])

    if rows == 1 or rows == 0 or cols == 1 or cols == 0:
        return True

    initial_row = arr[0][:cols-1]

    for rw in range(1, rows):
        if arr[rw][1:] != initial_row:
            return False
        else:
            initial_row = [arr[rw][0]] + initial_row[:len(initial_row)-1]

    return True """


inpt = [[1, 2, 3, 4],
        [5, 1, 2, 3],
        [6, 5, 1, 2]]
# OP = True
print(isToeplitz(inpt))
