from typing import List

"""
Problem Name: Sentence Reverse 

Problem Section: Array

Problem Statement:
You are given an array of characters arr that consists of sequences of characters separated by space characters.
Each space-delimited sequence of characters defines a word.
Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Example:
input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

revarr = ['e', 'c', 'i', 't', 'c', 'a', 'r', 'p', '  ', 's', 'e', 'k', 'a', 'm', '  ', 't', 'c', 'e', 'f', 'r', 'e', 'p']

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]


Resources:
"""

""" runtime """

# Solution techniques are

# Time complexity : O(n) Space complexity : O(1)


def rev_subarray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def reverse_words(arr):
    arr.reverse()
    arr_len = len(arr)
    start = None

    for i in range(0, arr_len):
        if arr[i].isspace():
            if start is not None:
                rev_subarray(arr, start, i-1)
                start = None
        elif i == arr_len-1:
            if start is not None:
                rev_subarray(arr, start, i)
        elif start is None:
            start = i

    return arr


# arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
#        'm', 'a', 'k', 'e', 's', '  ',
#        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
arr = ["h", "e", "l", "l", "o"]
print(reverse_words(arr))
