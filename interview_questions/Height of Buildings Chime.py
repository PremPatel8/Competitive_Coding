"""
### Problem Statement:
Given a list of numbers where each number represents the height of a building, and we are looking to the right, 
a taller building will block the view of the buildings behind it. Write a function that outputs the highest building each building can see; 
if a building cannot see any taller buildings, output -1 for that building.
"""

"""
Complexity Analysis

Time Complexity: O(n). Even though there is a nested while loop, each building is pushed onto and popped from the stack exactly once.

Space Complexity: O(n) to store the stack in the worst-case scenario (e.g., a decreasing sequence of buildings like [10, 8, 6, 4]).
"""

def highest_visible_building(heights):
    n = len(heights)
    highest_building = [-1] * n
    # Monotonic Decreasing Stack - Stores indices of unblocked buildings
    unblocked_buildings_index = []

    for i in range(n):
        # If current building is taller than the building on top of stack,
        # it 'blocks' the view and is the tallest thing that building can see.
        while unblocked_buildings_index and heights[i] > heights[unblocked_buildings_index[-1]]:
            prev_index = unblocked_buildings_index.pop()
            highest_building[prev_index] = heights[i]
        
        unblocked_buildings_index.append(i)
        
    return highest_building

# Example: [3, 4, 6, 2]
# Building 3 sees 4. 4 is taller, so it blocks the view. Result: 4.
# Building 4 sees 6. 6 is taller, so it blocks the view. Result: 6.
# Building 6 sees 2. 2 is shorter, so it doesn't block. 
# But there's nothing taller than 6. Result: -1.
# Building 2 has nothing to its right. Result: -1.

heights = [10, 5, 2, 7]
result = highest_visible_building(heights)
expected = [-1, 7, 7, -1]
print(result == expected)

heights = [10,6,8,5,11,9]
result = highest_visible_building(heights)
expected = [11,8,11,11,-1,-1]
print(result == expected)