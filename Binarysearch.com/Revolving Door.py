from collections import defaultdict, deque

# bunny - 141 mili, 76.3%


class Solution:
    """ def solve(self, requests):
        buckets = defaultdict(lambda: [0, 0])

        for t, d in requests:
            buckets[t][d] += 1

        currDir = 1
        currTime = 0
        ret = []
        lst = sorted(buckets.items())

        for t, (exit, enter) in lst:
            if t > currTime:
                currDir = 1
                currTime = t
            if currDir == 1:
                if enter:
                    for _ in range(enter):
                        ret.append([currTime, 1])
                        currTime += 1
                    currDir = 1
                if exit:
                    for _ in range(exit):
                        ret.append([currTime, 0])
                        currTime += 1
                    currDir = 0
            else:
                if exit:
                    for _ in range(exit):
                        ret.append([currTime, 0])
                        currTime += 1
                    currDir = 0
                if enter:
                    for _ in range(enter):
                        ret.append([currTime, 1])
                        currTime += 1
                    currDir = 1

        return ret """

    """ def solve(self, requests):
        # events dict with key = time and value = [total no people of exiting at that time, total no of people entering at that time] - List/tuple
        events = defaultdict(lambda: [0, 0])
        for time, direction in requests:
            events[time][direction] += 1

        ans = []
        # default start position and time
        direction = 1
        time = 0

        # for t in events:
        #     print(f"{t} : {events[t]}")

        # sort events by time that they happend, so we start iterating from the earliest event to the final event
        for t in sorted(events):
            # print(f"t - {t}, time - {time}")

            # If the next request time is greater than tracked time, then that means more than one time unit has passed where no one used the door,
            # so we reset the door direction to the deault 'in' position and and set the tracked time to the request time
            if t > time:
                time = t
                direction = 1

            # print(f"time - {time}, direction - {direction}")

            # whichever is the current direction of the door [in or out], we deal with the people going in that direction first, then deal with the people going in the opposite direction at the given time
            # first is the no of people going in the same direction as the current direction of the door for time - t
            # second is the no of people going in the other direction for time - t

            
            # ^ - XOR operator
            # logical operator that will return 1 when the bits are different and 0 elsewhere

            # 1 ^ 1 = 0
            # 0 ^ 1 = 1
           
            first = events[t][direction]
            second = events[t][direction ^ 1]

            # print(f"second - {second}, first - {first}")

            for t in range(time, time + first):
                ans.append([t, direction])

            for t in range(time + first, time + first + second):
                ans.append([t, direction ^ 1])

            time += first + second

            # whenever we have people going in the oppsite direction of the current direction of door, we need to flip the door direction
            if second:
                direction ^= 1

        return ans """

    def solve(self, requests):
        if not requests:
            return []

        IN = 1
        OUT = 0
        ans = []
        d = defaultdict(list)

        for t, r in requests:
            d[t] += [r]

        requests = sorted(d.items(), key=lambda x: x[0])
        door = IN
        t = requests[0][0]

        for time_of_req, reqs in requests:

            if time_of_req > t:
                t = time_of_req
                door = IN

            if door == IN:
                reqs = reversed(sorted(reqs))
            else:
                reqs = sorted(reqs)

            for r in reqs:
                ans.append([t, r])
                t += 1

            door = r

        return ans


requests = [
    [1, 0],
    [2, 1],
    [5, 0],
    [5, 1],
    [2, 0]
]

# requests = [
#     [0, 0],
#     [0, 0]
# ]

# t: exit, enter

myobj = Solution()

print(myobj.solve(requests))
