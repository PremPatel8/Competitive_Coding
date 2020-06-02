from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        changeCounter = 0

        nodesPointingToZero = set()
        nodesPointingToZero.add(0)

        for citiPairs in connections:
            a = citiPairs[0]
            b = citiPairs[1]

            if a in nodesPointingToZero and b != 0:
                changeCounter += 1
                nodesPointingToZero.add(b)
            elif b in nodesPointingToZero:
                nodesPointingToZero.add(a)

        return changeCounter


myclass = Solution()

# print(myclass.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(myclass.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
