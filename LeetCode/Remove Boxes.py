from typing import List

"""
Problem Name: Remove Boxes

Problem URL: https://leetcode.com/problems/remove-boxes/

Problem Section: Array, DP, Memoization

Problem Difficulty: Hard

Problem Statement:
You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. 
Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), 
remove them and get k * k points.

Return the maximum points you can get.

Example 1:
Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)


Constraints:
1 <= boxes.length <= 100
1 <= boxes[i] <= 100


Resources:

"""


class Solution:
    """
    Solution technique: Brute Force Recursive Approach [Time Limit Exceeded]

    Time & Space Complexity:
    Time - O(n!)
    Space - O(n^2)

    Runtime:
    """

    def removeBoxes(self, boxes: List[int]) -> int:
        return self.remove(boxes)

    def remove(self, boxes):
        lenBoxes = len(boxes)
        res = 0

        if lenBoxes == 0:
            return 0

        for startIdx in range(lenBoxes):
            # find end index of matching no sequence
            endIdx = self.endIndex(startIdx, startIdx+1, lenBoxes, boxes)

            matchSeqLen = endIdx-startIdx

            # Copy all remaining nos while skipping the matching no sequence
            newboxes = self.filterBoxes(
                lenBoxes, startIdx, endIdx, boxes)

            res = max(res, (matchSeqLen * matchSeqLen) + self.remove(newboxes))

        return res

    def endIndex(self, startIdx, endIdx, lenBoxes, boxes):
        while endIdx < lenBoxes and boxes[startIdx] == boxes[endIdx]:
            endIdx += 1
        return endIdx

    def filterBoxes(self, lenBoxes, startIdx, endIdx, boxes):
        newboxes = []
        k = 0

        while k < lenBoxes:
            if k == startIdx:
                k = endIdx

            if k < lenBoxes:
                newboxes.append(boxes[k])

            k += 1

        return newboxes


myobj = Solution()
inpt = [1, 3, 2, 2, 2, 3, 4, 3, 1]
# op = 23
print(myobj.removeBoxes(inpt))
"""
import file_name
def test_name():
    assert file_name.Solution().functionName(val) == OP
"""
