from collections import Counter, defaultdict


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

    # Alt solution using Counter which should be a O(n) time complexity compared to sorting
    # Your code took 396 milliseconds — faster than 11.02% in Python,
    # this sol is slower because for small number of strings and small sized strings creating a Counter is a slower than just sorting the strings

    def solve_alt(self, words):
        counter_freq_dict = defaultdict(int)

        for word in words:
            charCounter = Counter(word)

            counter_freq_dict[frozenset(charCounter.items())] += 1

        return max(counter_freq_dict.values())
