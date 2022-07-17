from collections import defaultdict


class Solution:
    def solve(self, words):
        anagramFreqDict = defaultdict(int)

        for word in words:
            anagramFreqDict[''.join(sorted(word))] += 1

        # Your code took 108 milliseconds — faster than 96.83% in Python
        # maxKey =  max(anagramFreqDict, key=anagramFreqDict.get)
        # return anagramFreqDict[maxKey]

        # Your code took 106 milliseconds — faster than 98.81% in Python
        return max(anagramFreqDict.values())
