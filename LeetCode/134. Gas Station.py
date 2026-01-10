"""
[134. Gas Station](https://leetcode.com/problems/gas-station/) There are `n` gas stations along a circular route, where the amount of gas at the `ith` station is `gas[i]`.
 
You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `ith` station to its next `(i + 1)th` station. You begin the journey with an empty tank at one of the gas stations.
 
Given two integer arrays `gas` and `cost`, return  *the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return*  `-1`. If there exists a solution, it is **guaranteed** to be **unique**.
 
**Example 1:**
**Input:** gas = [1,2,3,4,5], cost = [3,4,5,1,2]
**Output:** 3
**Explanation:**
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
 
**Example 2:**
**Input:** gas = [2,3,4], cost = [3,4,3]
**Output:** -1
**Explanation:**
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 
**Constraints:**
 
- `n == gas.length == cost.length`
- `1 <= n <= 105`
- `0 <= gas[i], cost[i] <= 104`
- The input is generated such that the answer is unique.
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total gas available across all stations is less than the total cost required to travel between them, then it's impossible to complete the circuit.
        total_tank = 0
        
        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # If current tank goes negative, reset start to next station
            # If you start at station A and run out of gas before reaching station B, then any station between A and B (inclusive) cannot be a valid starting point. 
            # You should try starting from B + 1 instead.
            
            """        
            From A to A+1: we had gas[A] - cost[A] leftover after reaching A+1.
            Then we continued from A+1 onward, eventually failing before B.
            So when we started at A, our tank at A+1 was ≥ 0
            But if we start at A+1 directly, our tank starts at 0 + gas[A+1] — which is less than or equal to the amount we had when arriving at A+1 from A
            Since even the more favorable scenario (starting at A, arriving at A+1 with extra gas) still failed before B, then the less favorable scenario (starting at A+1 with no prior surplus) must also fail before or at B.
            Thus, A+1 cannot be a valid start.
            The same logic applies to A+2, A+3, ..., B−1 — none of them can work, because you’d have even less accumulated gas when starting from them than you did when passing through them from A.
            """
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        return start if total_tank >= 0 else -1