"""
each num = abs(num) = rocket size, + = right, - = left

If two rockets collide, the smaller one will disappear and the larger one will continue on its course unchanged. 

If they are the same size and they collide, they'll both explode (both numbers are removed). 

If two rockets are moving in the same direction, they will never collide. 
"""


class Solution:
    def solve(self, nums):
        if len(nums) < 2:
            return nums

        res = []

        for num in nums:
            if num < 0:
                if res and res[-1] > 0:
                    for lastRocket in reversed(res):
                        lastRocketValue = abs(lastRocket)
                        lastRocketDir = "left" if lastRocket < 0 else "right"
                        if lastRocketValue == abs(num) and lastRocketDir == "right":
                            res.pop()
                            num = 0
                            break
                        elif lastRocketValue < abs(num) and lastRocketDir == "right":
                            res.pop()
                        elif lastRocketValue > abs(num) and lastRocketDir == "right":
                            num = 0
                            break
                    if num != 0:
                        res.append(num)
                else:
                    res.append(num)
            else:
                res.append(num)

        return res


# nums = [-1, 1]
# # Op = [-1, 1]

nums = [-3, 1, -3]
# Op = [-3, -3]

myobj = Solution()
print(myobj.solve(nums))
