from collections import deque
from itertools import zip_longest

# string based sol Your code took 4 milliseconds — faster than 23.07% in Python
""" class Solution:
    def solve(self, a, b):
        carry = 0
        res = ""

        for a_ch, b_ch in zip_longest(reversed(a), reversed(b), fillvalue=0):

            temp_sum = int(a_ch)+int(b_ch)+carry

            if temp_sum > 9:
                res = str(temp_sum % 10)+res
                carry = 1
            else:
                res = str(temp_sum)+res
                carry = 0

        if carry != 0:
            tmp = str(carry)
            res = tmp+res

        return res """


# deque based sol Your code took 5 milliseconds — faster than 19.34% in Python
# class Solution:
#     def solve(self, a, b):
#         carry = 0
#         res = deque([])

#         for a_ch, b_ch in zip_longest(reversed(a), reversed(b), fillvalue=0):

#             temp_sum = int(a_ch)+int(b_ch)+carry

#             digit = temp_sum % 10
#             carry = temp_sum//10

#             res.appendleft(str(digit))

#         if carry != 0:
#             res.appendleft('1')

#         return "".join(res)


# list based sol Your code took 5 milliseconds — faster than 19.34% in Python
class Solution:
    def solve(self, a, b):
        carry = 0
        res = []

        for a_ch, b_ch in zip_longest(reversed(a), reversed(b), fillvalue=0):

            temp_sum = int(a_ch)+int(b_ch)+carry

            digit = temp_sum % 10
            carry = temp_sum//10

            res.append(str(digit))

        if carry != 0:
            res.append('1')

        return "".join(reversed(res))


# a = "12"
# b = "23"

# a = "1"
# b = "9"

a = "17"
b = "3"

myobj = Solution()

print(myobj.solve(a, b))
