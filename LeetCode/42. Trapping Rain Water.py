from typing import List


"""
Problem Name: 42. Trapping Rain Water

Problem Section: Array, Two Pointers, Stack

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Resources:

"""

# Solution techniques are Dynamic Programming (2 for loops to create left max and right max arrays), Using stacks, Using 2 pointers
# Time complexity : O(n) Space complexity : O(1) Optimized solution using 2 pointers

    
# Brute Force Solution
""" 
Time complexity: O(n2). For each element of array, we iterate the left and right parts.
Space complexity: O(1) extra space.
"""
class Solution:
    def trap(self, height):
        ans = 0
        size = len(height)
        
        """ 
        why the range starts at 1 and ends at size - 2:
        At index 0 (the first bar) → you can’t trap water, because there’s no bar to the left.
        At index size - 1 (the last bar) → you also can’t trap water, because there’s no bar to the right.
        """
        for i in range(1, size - 1):
            left_max = 0
            right_max = 0
            
            # Search the left part for max bar size
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
                
            # Search the right part for max bar size
            for j in range(i, size):
                right_max = max(right_max, height[j])
                
            # The amount of water that can be trapped at for each element in the array,
            # is equal to the minimum of maximum height of bars on both the left and right sides of the current index bar minus its own height.
            ans += min(left_max, right_max) - height[i]
        return ans
    
    
# Dynamic Programming Solution / Prefix & Suffix Arrays ?
""" 
Time complexity: O(n).
    We store the maximum heights upto a point using 2 iterations of O(n) each.
    We finally update ans using the stored values in O(n).

Space complexity: O(n) extra space.
    Additional O(n) space for left_max and right_max arrays than in Approach 1.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        ans = 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size
        
        # Record the max bar from the left upto given index
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])
        
        # # Record the max bar from the given index to the right
        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        
        # Calculate the trapped water
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans
    
# Monotonically increasing Stack Solution, difficult to induerstand
""" 
Time complexity: O(n).
    Single iteration of O(n) in which each bar can be touched at most twice(due to insertion and deletion from stack) and insertion and deletion from stack takes O(1) time.
Space complexity: O(n). Stack can take upto O(n) space in case of stairs-like or flat structure.

"""
class Solution:
    def trap(self, height):
        ans = 0
        current = 0
        st = []
        while current < len(height):
            while len(st) != 0 and height[current] > height[st[-1]]:
                top = st[-1]
                st.pop()
                if len(st) == 0:
                    break
                distance = current - st[-1] - 1
                bounded_height = (
                    min(height[current], height[st[-1]]) - height[top]
                )
                ans += distance * bounded_height
            st.append(current)
            current += 1
        return ans
    
    
# Two Pointer Solution, Most Efficient
""" 
Complexity analysis
Time complexity: O(n) Single iteration of O(n)
Space complexity: O(1) extra space. Only constant space required for left, right, left_max and right_max
"""

# Example input - height = [0,1,0,2,1,0,1,3,2,1,2,1]
class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 0:
            return 0

        ans = left_max = right_max = 0

        left = 0
        right = len(height)-1
        
        """ 
        As long as right_max[i]>left_max[i], the water trapped depends upon the left_max, and similar is the case when left_max[i]>right_max[i]
        So, we can say that if there is a larger bar at one end (say right), 
        we are assured that the water trapped would be dependant on the difference between the max height min curr height of bar in current direction (from left to right).
        As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left).
        """

        while left < right:
            # If the height of the curr left bar is less than the height of curr right bar,
            # Then the water trapped would depend on the max left bar seen so far
            if height[left] < height[right]:
                # If current bar is taller or the same height than the current max left bar seen so far, then just make it the left_max as no water could be trapped
                if height[left] >= left_max:
                    left_max = height[left]
                # Else if the current bars height is less than the left max, then water will be trapped, so update the answer
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max-height[right]
                right -= 1

        return ans


myobj = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(myobj.trap(height))
# Output: 6
