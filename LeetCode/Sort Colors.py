from typing import List

"""
Problem Name: Sort Colors

Problem Section: Sorting and Searching

Problem Statement:
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

""" 87 / 87 test cases passed.
	Status: Accepted
Runtime: 40 ms
Memory Usage: 13.8 MB """

""" 
    0 = red
    1 = white
    2 = blue
     """

# dutch partitioning problem solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white = 0, 0
        blue = len(nums)-1

        while white <= blue:
            # If the current list object is Red, which is less than mid (white) and should come before it
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
             # If the current list object is White which is equal to mid and hence in the correct position already
            elif nums[white] == 1:
                white += 1
            else:
                # If the current list object is Blue which is greater than mid (white) and should come after it.
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

        print(nums)


myobj = Solution()

input = [2, 0, 2, 1, 1, 0]

myobj.sortColors(input)
