# Binarysearch.com Most Frequent Number in Intervals - Line Sweep approach

class Solution:
    def solve(self, intervals):
        OPEN, CLOSE = 0, 1
        active = max_active = 0

        events = []

        for s, e in intervals:
            events.append([s, OPEN])
            events.append([e, CLOSE])
        
        events.sort()

        for x, cmd in events:
            active += 1 if cmd == OPEN else -1
            max_active = max(max_active, active)

        for x, cmd in events:
            active += 1 if cmd == OPEN else -1
            if active == max_active:
                return x

        return 0

