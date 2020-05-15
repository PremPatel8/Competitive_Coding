def binary_array_to_number(arr):
    result = 0

    for i, val in enumerate(reversed(arr)):
        if val:
            result += 2**i
          
    return result

print(binary_array_to_number([0, 1, 0, 1]))