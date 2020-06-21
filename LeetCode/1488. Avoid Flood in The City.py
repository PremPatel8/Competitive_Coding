from typing import List
from collections import defaultdict


class Solution:
    def get_next_empty_day(self, lake_full_day, emptyDay):
        for day in emptyDay:
            if day > lake_full_day:
                return day

        return -1

    def avoidFlood(self, rains: List[int]) -> List[int]:
        lake_day_status = defaultdict(lambda: -1)
        emptyDay = []
        output = []

        for day, rlake in enumerate(rains):
            # if it rains that day
            if rlake > 0:
                # if the lake on which it rains that day is empty
                if lake_day_status[rlake] == -1:
                    lake_day_status[rlake] = day
                    output.append(-1)
                # if the lake on which it rains that day is already full
                elif lake_day_status[rlake] >= 0:
                    # if a empty day after the day the lake got full is available to use
                    next_empty_day = self.get_next_empty_day(
                        lake_day_status[rlake], emptyDay)
                    if next_empty_day >= 0:
                        emptyDay.remove(next_empty_day)
                        lake_day_status[rlake] = day
                        output[next_empty_day] = rlake
                        output.append(-1)
                    # Lake floods over since no empty day after it available to use
                    else:
                        return []
            elif rlake == 0:
                emptyDay.append(day)
                output.append("p")

        return [1 if x == "p" else x for x in output]


myClassObj = Solution()
# rains = [1, 2, 0, 0, 2, 1]
rains = [69, 0, 0, 0, 69]
print(myClassObj.avoidFlood(rains))
