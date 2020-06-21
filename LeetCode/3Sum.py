# Solution using 2 pointer
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         output = []
#         length = len(nums)

#         for xitr in range(length-2):
#             if nums[xitr] > 0:
#                 break

#             if xitr == 0 or xitr > 0 and nums[xitr] != nums[xitr-1]:
#                 lwrBnd = xitr+1
#                 uprBnd = length-1
#                 # ansSum = 0-x

#                 while lwrBnd < uprBnd:
#                     total = nums[xitr] + nums[lwrBnd] + nums[uprBnd]

#                     if total < 0:
#                         lwrBnd += 1
#                     elif total > 0:
#                         uprBnd -= 1
#                     elif total == 0:
#                         output.append([nums[xitr], nums[lwrBnd], nums[uprBnd]])

#                         while lwrBnd < uprBnd and nums[lwrBnd] == nums[lwrBnd+1]:
#                             lwrBnd += 1
#                         while lwrBnd < uprBnd and nums[uprBnd] == nums[uprBnd-1]:
#                             uprBnd -= 1

#                         lwrBnd += 1
#                         uprBnd -= 1

#         return output

# Solution using Dict / Hash Map / Set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        import collections
        count = collections.Counter(nums)
        # [0, 0, 0]
        ans = []
        if count[0] > 2:
            ans.append([0, 0, 0])
        # [x, x, -2x]
        for key in count.keys():
            if count[key] > 1 and count[-key*2] > 0 and key != 0:
                ans.append([key, key, -2*key])
        # [x, y, -x-y]
        keys = list(count.keys())
        keys.sort()
        s = set(keys)
        for i in range(len(keys)-1):
            for j in range(i+1, len(keys)):
                num = -keys[i]-keys[j]
                if num <= keys[j]:
                    break
                if num in s:
                    ans.append([keys[i], keys[j], num])
                
        return ans