""" Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i. 

All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

We want to calculate the probability that the two boxes have the same number of distinct balls. """

from typing import List
from itertools import permutations
from collections import defaultdict


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        ballSet = []
        numerator = 0
        i = 1

        for b in balls:
            for _ in range(b):
                ballSet.append(i)
            i += 1

        permList = list(set(permutations(ballSet)))

        denominator = len(permList)

        for pl in permList:
            Left = pl[:len(pl)//2]
            Right = pl[len(pl)//2:]

            if len(set(Left)) == len(set(Right)):
                numerator += 1

        return numerator/denominator


myClassObj = Solution()

# print(myClassObj.getProbability([2, 1, 1]))
# print(myClassObj.getProbability([1, 2, 1, 2]))
print(myClassObj.getProbability([6, 6, 6, 6, 6, 6]))
