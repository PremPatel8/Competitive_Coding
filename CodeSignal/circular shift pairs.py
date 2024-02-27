from collections import Counter

"""
A circular shift moves some of the digits in a number to the beginning of the number, and shifts all other digits forward to the next position. For example, all of the circular shifts of 564 are 564, 645, 456.

Lets say two numbers of equal length a and b are circular pairs if a can become b via circular shifting. Using the example above, the circular pairs of 564 are 645 and 456.

Given an array of positive integers nums, count the number of circular pairs i and j where 0 <= i < j < len(nums)

For example, circular_shifts([13, 5604, 31, 2, 13, 4560, 546, 654, 456]) should return 5. With the pairs being (13, 31), (13, 13), (5604, 4560), (31, 13), (546, 654).
"""

def biggestCircularShiftedNumber(num):
    maxNo = num

    num_str = str(num)

    for _ in num_str:
        shiftedNo = int(num_str[-1] + num_str[0:-1])

        maxNo = max(maxNo, shiftedNo)
            
    return maxNo

def circularShiftPairs(numbers):
    total = 0
    
    maxShiftedNos = [biggestCircularShiftedNumber(no) for no in numbers]

    maxShiftedNosFreq = Counter(maxShiftedNos)

    total = sum(freq for freq in maxShiftedNosFreq.values() if freq > 1)

    return total



numbers = [13, 5604, 31, 2, 13, 4560, 546, 654, 456]

result = circularShiftPairs(numbers)

print(f"result = {result}")