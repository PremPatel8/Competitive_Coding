"""
853. Car Fleet
[853. Car Fleet](https://leetcode.com/problems/car-fleet/) There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`.
 
You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the `ith` car and `speed[i]` is the speed of the `ith` car in miles per hour.
 
A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
 
A **car fleet** is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum** speed of any car in the fleet.
 
If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
 
Return the number of car fleets that will arrive at the destination.
 
**Example 1:**
**Input:**target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
 
**Output:**3
 
**Explanation:**
 
- The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at `target`.
- The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
- The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches `target`.
 
**Example 2:**
**Input:**target = 10, position = [3], speed = [3]
 
**Output:**1
 
**Explanation:**
 
There is only one car, hence there is only one fleet.
 
**Example 3:**
**Input:**target = 100, position = [0,2,4], speed = [4,2,1]
 
**Output:**1
 
**Explanation:**
 
- The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
- Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches `target`.
 
**Constraints:**
 
- `n == position.length == speed.length`
- `1 <= n <= 105`
- `0 < target <= 106`
- `0 <= position[i] < target`
- All the values of `position` are **unique**.
- `0 < speed[i] <= 106`
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # tuples of (position, speed), sorted by position (smallest first = farthest from target, largest last = closest to target).
        cars = sorted(zip(position, speed))

        # time each car would take to reach the target if it drove alone
        # In Python2 `/` does integer division (it truncates the result).
        # 5 / 2   # → 2, not 2.5, which we don't want as we want exact time here.
        # Hence we can do float(target-p) to prevent the truncation
        # In Python3 `/` does floating-point division by default so wrapping it in float is not needed.
        times = [(target - p) / s for p, s in cars]



        """
        Why we only compare “closest vs. next closest”
        Think about processing cars from right to left (closest to the target first):
        - Suppose Car A is closest to the target, with time tA.
        - Car B is behind it, with time tB.

        Two possibilities:
        1. If tB > tA:
        Car B takes longer to arrive, so it will never catch Car A. → Car A is its own fleet.

        2. If tB ≤ tA:
        Car B will eventually catch Car A, so they merge into one fleet, arriving at time tA.

        What about a car even further back, Car C?
        - Car C can only catch Car A if it can first catch Car B.
        - But since we already merge B with A (if possible), Car C just compares against the merged fleet’s arrival time.
        - That’s why we keep updating times[-1] = lead in the code — it represents the whole fleet ahead.
        """

        ans = 0
        while len(times) > 1:
            # We pop from the right of the list, so the time taken by the car closest to the target
            lead = times.pop()
            # times[-1] is the second closest cars time to the target
            # if lead arrives sooner (it's time to target is smaller than the that of the time behind it), it can't be caught
            if lead < times[-1]:
                ans += 1
            else:
                # it represents the whole fleet ahead.
                times[-1] = lead # else, fleet arrives at later time 'lead'

        return ans + bool(times) # remaining car is fleet (if it exists)