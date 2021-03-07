class Solution:
    """ 152 milliseconds — faster than 24.84% in Python """
    """ def solve(self, nums):
        a1 = sum(nums[i] > nums[(i + 1) % len(nums)]
                 for i in range(len(nums))) <= 1
        a2 = sum(nums[i] < nums[(i + 1) % len(nums)]
                 for i in range(len(nums))) <= 1
        return a1 or a2 """

    """ 53 milliseconds — faster than 89.17% in Python """

    def solve(self, nums):
        break_point = 0
        arrLen = len(nums)
        clockwise_result = anticlockwise_result = True

        if arrLen <= 1:
            return True

        for i in range(arrLen):
            if nums[i] > nums[(i + 1) % arrLen]:
                if break_point < 1:
                    break_point += 1
                else:
                    clockwise_result = False
                    break

        break_point = 0

        for i in range(arrLen):
            if nums[i] < nums[(i + 1) % arrLen]:
                if break_point < 1:
                    break_point += 1
                else:
                    anticlockwise_result = False
                    break

        return clockwise_result or anticlockwise_result

    """ 0  1  2  3
nums =     [4, 1, 2, 3] """


myobj = Solution()
nums = [4, 1, 2, 3]
print(myobj.solve(nums))
