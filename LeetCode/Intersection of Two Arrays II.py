from typing import List
from collections import Counter
from collections import defaultdict
"""
Problem Name: Intersection of Two Arrays II

Problem Section: Array

Problem Statement:
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Resources:

"""

""" 61 / 61 test cases passed.
	Status: Accepted
Runtime: 44 ms
Memory Usage: 14.1 MB """

# Solution techniques are

# Time complexity : O(n*2) Space complexity : O() My optimized solution using counter and intersection


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        intersection = count1 & count2

        return list(intersection.elements())


# Frequency Counter solution with optimization to pick smaller list to generate smaller dict/counter and save space
# Time - O(n+m), Space - O(min(n,m))
# where n and mare the lengths of the arrays. 
# We iterate through the first, and then through the second array; 
# insert and lookup operations in the hash map take a constant time.
""" 55 / 55 test cases passed.
	Status: Accepted
Runtime: 44 ms
Memory Usage: 14.3 MB """


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        (smallerNums, largerNums) = (nums1, nums2) if nums1 < nums2 else (nums2, nums1)

        # freqCount = defaultdict(int)
        # for num in smallerNums:
        #     freqCount[num] += 1

        freqCount = Counter(smallerNums)

        for num in largerNums:
            if num in freqCount and freqCount[num] > 0:
                freqCount[num] -= 1
                res.append(num)

        return res

# Sorting solution
""" You can recommend this method when the input is sorted, or when the output needs to be sorted. 
Here, we sort both arrays (assuming they are not sorted) and use two pointers to find common numbers in a single scan. """
""" 
Time Complexity: O(nlog⁡n+mlog⁡m), where n and m are the lengths of the arrays. We sort two arrays independently, and then do a linear scan.

Space Complexity: from O(log⁡n+log⁡m) to O(n+m), depending on the implementation of the sorting algorithm. 
For the complexity analysis purposes, we ignore the memory required by inputs and outputs.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = k = 0

        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                k += 1
                i += 1
                j += 1
        
        return nums1[:k]


myobj = Solution()
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
nums1 = [2, 1]
nums2 = [1, 2]
print(myobj.intersect(nums1, nums2))
