from typing import DefaultDict


class Solution:
    def solve(self, nums):
        mydict = DefaultDict(list)
        maxpair_sum = 0

        for idx, num in enumerate(nums):
            mydict[num].append(idx)

        keys = list(mydict.keys())

        for idx, i_key in enumerate(keys):
            i_indexes = mydict[i_key]

            if len(i_indexes) > 1:
                lowestdiff = float("inf")

                for i in range(len(i_indexes)-1):
                    lowestdiff = min(
                        lowestdiff, abs(i_indexes[i] - i_indexes[i+1]))

                maxpair_sum = max(maxpair_sum, (i_key*2 - lowestdiff))

            for j in range(idx+1, len(keys)):
                j_key = keys[j]

                if (i_key+j_key)-1 < maxpair_sum:
                    continue
                else:
                    maxpair_sum = max(maxpair_sum, ((
                        i_key+j_key) - self.closestIndexDiff(i_indexes, mydict[j_key])))

        return maxpair_sum

    def closestIndexDiff(self, i_indexes, j_indexes):
        i = j = 0
        minDiff = float("inf")
        i_len = len(i_indexes)
        j_len = len(j_indexes)

        while(i < i_len and j < j_len):
            diff = abs(i_indexes[i] - j_indexes[j])
            minDiff = min(minDiff, diff)

            if i_indexes[i] < j_indexes[j]:
                i += 1
            else:
                j += 1

        return minDiff


myobj = Solution()
# nums = [5, 5, 1, 1, 1, 7]  # ans - 9
# nums = [6, 9, 6, 3, 6, 6, 3, 4, 4, 5]  # ans - 14
# nums = [9, 1, 2, 10, 6, 9, 3, 3, 7, 7]  # ans - 17
nums = [3, 6, 5, 2, 10, 2, 6, 10, 8, 10]  # ans - 18
print(myobj.solve(nums))

#    0  1  2  3  4  5
# [5, 5, 1, 1, 1, 7]
# 5 - 0, 1
# 1 - 2, 3, 4
# 7 - 5
