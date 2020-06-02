from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxHeight = maxWidth = 0
        horizontalCuts.sort()
        verticalCuts.sort()

        for i, v in enumerate(horizontalCuts):
            leftEdge = v if i == 0 else abs(v-horizontalCuts[i-1])
            rightEdge = h-v if i == len(horizontalCuts) - \
                1 else abs(v-horizontalCuts[i+1])

            maxHeight = max(maxHeight, leftEdge, rightEdge)

        for i, v in enumerate(verticalCuts):
            leftEdge = v if i == 0 else abs(v-verticalCuts[i-1])
            rightEdge = w-v if i == len(verticalCuts) - \
                1 else abs(v-verticalCuts[i+1])

            maxWidth = max(maxWidth, leftEdge, rightEdge)

        return (maxWidth*maxHeight) % (10**9 + 7)


myclass = Solution()

# print(myclass.maxArea(5, 4, [1, 2, 4], [1, 3]))
print(myclass.maxArea(5, 4, [3, 1], [1]))
