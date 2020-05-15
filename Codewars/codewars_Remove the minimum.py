def remove_smallest(numbers):
    if not numbers:
        return []
    
    # nbrs = numbers.copy()
    # nbrs.sort()

    # smallest = nbrs[0]

    pstn = numbers.index((sorted(numbers))[0])

    return numbers[:pstn]+numbers[pstn+1:]
    

print(remove_smallest([5, 3, 2, 1, 4]))