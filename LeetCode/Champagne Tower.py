from typing import List

"""
Problem Name: 799. Champagne Tower

Problem URL: https://leetcode.com/problems/champagne-tower/

Problem Section: Simulation, DP

Problem Statement:
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

Resources:

runtime: 
312 / 312 test cases passed.
	Status: Accepted
Runtime: 96 ms
Memory Usage: 14.3 MB
"""

# Solution techniques are Simulation

# Time complexity : O() Space complexity : O()
""" 
Time Complexity: O(R^2), where RRR is the number of rows. As this is fixed, we can consider this complexity to be O(1).
Space Complexity: O(R^2), or O(1) by the reasoning above.
 """


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = 0
        if poured == 0:
            return 0

        if query_row == 0:
            return min(1, poured)

        tower = [[0] * k for k in range(1, 102)]

        """
        keep track of the total amount of champagne that flows through a glass. For example, if poured = 10 cups are poured at the top, then the total flow-through of the top glass is 10; the total flow-through of each glass in the second row is 4.5, and so on.
        
         if a glass has flow-through X, then Q = (X - 1.0) / 2.0 quantity of champagne will equally flow left and right. We can simulate the entire pour for 100 rows of glasses. A glass at (r, c) will have excess champagne flow towards (r+1, c) and (r+1, c+1).
        """

        tower[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r+1):
                q = (tower[r][c] - 1.0) / 2.0

                if q > 0:
                    tower[r+1][c] += q
                    tower[r+1][c+1] += q

        return min(1, tower[query_row][query_glass])


myobj = Solution()

poured = 100000009
query_row = 33
query_glass = 17
# Output: 1.00000
print(myobj.champagneTower(poured, query_row, query_glass))
