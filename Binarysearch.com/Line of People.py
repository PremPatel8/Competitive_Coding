# Line of People

class Solution:
    def solve(self, n, a, b):
        if b < a:
            return b+1
        elif b > a:
            return a-1
        
        return -1