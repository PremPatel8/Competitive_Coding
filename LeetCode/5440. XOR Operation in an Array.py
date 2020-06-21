class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = 0
        
        for i in range(n):
            output = output ^ (start+2*i)
        
        return output