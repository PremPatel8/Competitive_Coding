# Line of People

class Solution:
    def solve(self, n, a, b):
        b_end_point = b-1
        a_start_point = n-a

        # print(f"a_start_point = {a_start_point}")
        # print(f"b_end_point = {b_end_point}")

        if b_end_point < a_start_point:
            return b_end_point+2
        elif b_end_point >= a_start_point:
            return a_start_point
        
        return -1


n = 343914375
a = 1
b = 343914375

myobj = Solution()
print(myobj.solve(n,a,b))