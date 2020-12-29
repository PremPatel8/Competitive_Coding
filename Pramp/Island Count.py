"""
My Solution:
Loop through matrix from 0,0 till end
if index element 1 : start DFS checking
if any neighbour 1 recursively iterate till no more neighbours 1
replace each 1 with diff symbol to prevent loops
increment island counter after returning from DFS
"""


def get_number_of_islands(binaryMatrix):
    islands = 0
    rows = len(binaryMatrix)
    columns = len(binaryMatrix[0])

    def dfs(row, col):
        #print(row, col)
        if row >= rows or row < 0 or col >= columns or col < 0 or binaryMatrix[row][col] != 1:
            return

        binaryMatrix[row][col] = -1

        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)

        return

    for row in range(rows):
        for col in range(columns):
            currEle = binaryMatrix[row][col]

            if currEle == 1:
                dfs(row, col)
                islands += 1

    return islands


inpt = [[0,    1,    0,    1,    0],
        [0,    0,    1,    1,    1],
        [1,    0,    0,    1,    0],
        [0,    1,    1,    0,    0],
        [1,    0,    1,    0,    1]]

print(get_number_of_islands(inpt))
