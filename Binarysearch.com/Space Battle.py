"""
each num = abs(num) = rocket size, + = right, - = left

If two rockets collide, the smaller one will disappear and the larger one will continue on its course unchanged. 

If they are the same size and they collide, they'll both explode (both numbers are removed). 

If two rockets are moving in the same direction, they will never collide. 
"""

# Your code took 165 milliseconds — faster than 97.66% in Python


class Solution:
    def solve(self, nums):
        if len(nums) < 2:
            return nums

        stack = []

        for num in nums:
            if num > 0:
                stack.append(num)
            else:
                absNumVal = abs(num)
                skipFlag = False
                while stack and 0 < stack[-1] <= absNumVal:
                    currVal = stack.pop()
                    if currVal == absNumVal:
                        skipFlag = True
                        break

                if not skipFlag and (not stack or stack[-1] < 0):
                    stack.append(num)

        return stack

    # Your code took 134 milliseconds — faster than 99.71% in Python
    # optimized stack solution with extra space
    # def solve(self, nums):
    #         stack = []
    #         right_to_left = []

    #         for num in nums:
    #             if num > 0:
    #                 stack.append(num)
    #             else:
    #                 still_going = True
    #                 while stack and stack[-1] <= -num:
    #                     current = stack.pop()
    #                     if current == -num:
    #                         still_going = False
    #                         break

    #                 if not stack and still_going:
    #                     right_to_left.append(num)

    #         return right_to_left + stack


# nums = [-1, 1]
# # Op = [-1, 1]

nums = [-3, 1, -3]
# Op = [-3, -3]

myobj = Solution()
print(myobj.solve(nums))
