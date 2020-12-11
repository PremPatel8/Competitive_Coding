""" Merging 2 Packages

Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21

Constraints:

    [time limit] 5000ms

    [input] array.integer arr
        0 ≤ arr.length ≤ 100

    [input] integer limit

    [output] array.integer

 """


# def get_indices_of_item_wights(arr, limit):
#     seen = {}
#     output = []

#     for index, item in enumerate(arr):
#         comp = limit-item
#         # print(index, item)

#         if comp in seen:
#             # print(comp)
#             index_comp = seen[comp]
#             output.append(index)
#             output.append(index_comp)
#         else:
#             seen[item] = index

#     return output

def get_indices_of_item_wights(arr, limit):
    if not arr:
        return []

    seen = {}
    for i, a in enumerate(arr):
        if a in seen:
            return [i, seen[a]]
        else:
            seen[limit-a] = i
    return []


arr = [4, 6, 10, 15, 16]
lim = 21

print(get_indices_of_item_wights(arr, lim))
