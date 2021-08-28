from typing import List
from collections import Counter

"""
Problem Name: Fruit Into Baskets

Problem URL: https://leetcode.com/problems/fruit-into-baskets/

Problem Section: Two Pointer, Sliding Window, Array

Problem Difficulty: Medium

Problem Statement:
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.


Resources:

"""


class Solution:
    """
    Solution technique: My two pointer solution

    Time & Space Complexity:
    Time - O(n^2), because of the nested while loop within the outer while loop
    Space - O(1), since at most there will only be two fruits in the basket

    Runtime:
    90 / 90 test cases passed.
        Status: Accepted
    Runtime: 880 ms
    Memory Usage: 20.2 MB
    """

    # def totalFruit(self, fruits: List[int]) -> int:
    #     totalMaxFruit = 0
    #     i = 0

    #     if len(fruits) < 2:
    #         return 1

    #     while i <= (len(fruits)-2):
    #         print(f"i = {i}")

    #         currMaxFruit = 0
    #         basket = {}
    #         j = i

    #         while j < len(fruits):
    #             # if basket has less than two different fruits then add the fruit to the basket
    #             if len(basket) < 2:
    #                 basket[fruits[j]] = j
    #                 currMaxFruit += 1
    #             # if basket already has two different fruits, check if current fruit type is already in the basket
    #             elif fruits[j] in basket:
    #                 # if current fruit type is not a unbroken chain of the same fruit then we have to update it's left most index to it's current index
    #                 # since we can start from any tree but we cannot skip any trees and we have to pick one fruit from each tree while moving to the right
    #                 # So whenver we encounter a new type of fruit, we have to skip all fruits before the left most start index of the second last fruit
    #                 # 0123456
    #                 # 1211223
    #                 # for e.g. in the above sequence, when we encounter the new fruit 3, we have to move the left pointer to the left most unbroken start index
    #                 # of the second last fruit (fruit 2), which would be index 4, thus we would skip all fruits before the left most unroken index of fruit 2
    #                 if fruits[j-1] != fruits[j]:
    #                     basket[fruits[j]] = j
    #                 currMaxFruit += 1
    #             else:
    #                 break

    #             j += 1

    #         totalMaxFruit = max(totalMaxFruit, currMaxFruit)

    #         if(j == len(fruits)):
    #             break
    #         else:
    #             i = basket[fruits[j-1]]

    #     return totalMaxFruit

    """
    Solution technique: My two pointer optimized solution usin Dict to store left most unbroken start index

    Time & Space Complexity:
    Time - O(n), because of the nested while loop within the outer while loop
    Space - O(1), since at most there will only be three fruits in the basket
    
    Runtime:
    90 / 90 test cases passed.
	Status: Accepted
    Runtime: 784 ms
    Memory Usage: 20.2 MB
     """

    # def totalFruit(self, fruits: List[int]) -> int:
    #     if len(fruits) < 2:
    #         return 1

    #     left, res = 0, 0
    #     # dict mapping each fruit to it's left most unbroken start index
    #     basket = {}

    #     basket[fruits[0]] = 0

    #     for right in range(1, len(fruits)):
    #         if fruits[right-1] != fruits[right]:
    #             basket[fruits[right]] = right

    #         if len(basket) > 2:
    #             left = basket[fruits[right-1]]

    #             fruitsSlice = fruits[right-1:right+1]
    #             keyToDelete = [
    #                 key for key in basket.keys() if key not in fruitsSlice]

    #             # alt way to get the key to be deleted from dict
    #             # basketKeysSet = set(basket.keys())
    #             # fruitsSet = set(fruits[right-1:right+1])
    #             # keyToDelete = basketKeysSet-fruitsSet

    #             del basket[keyToDelete.pop()]

    #         res = max(res, right - left + 1)
    #     return res

    """ 
    Solution technique: Sliding Window optimized solution without using Dict / Hash Map 
    https://leetcode.com/problems/fruit-into-baskets/discuss/170745/Problem%3A-Longest-Subarray-With-2-Elements

    Time & Space Complexity:
    Time - O(n)
    Space - O(1)
    
    Runtime:
    90 / 90 test cases passed.
	Status: Accepted
    Runtime: 682 ms
    Memory Usage: 20.2 MB
    """

    # def totalFruit(self, fruits: List[int]) -> int:
    #     res = curr_fruit_count = last_fruit_count = secondLastFruit = lastFruit = 0

    #     for currFruit in fruits:
    #         if currFruit in (lastFruit, secondLastFruit):
    #             # if curr fruit is same as any of the last two fruits that have been collected
    #             # then we can add this fruit to the basket and increment the curr fruit count
    #             curr_fruit_count += 1
    #         else:
    #             # if this a new fruit not seen before, then we start a new sequence starting from
    #             # the last seen fruit, so curr fruit count becomes last seen fruit count + 1
    #             curr_fruit_count = last_fruit_count + 1

    #         if currFruit == lastFruit:
    #             last_fruit_count += 1
    #         else:
    #             last_fruit_count = 1
    #             secondLastFruit, lastFruit = lastFruit, currFruit

    #         res = max(res, curr_fruit_count)

    #     return res

    """ 
       Solution technique: Sliding Window optimized solution using Dict / Hash Map to store freq count
       https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements

       Time & Space Complexity:
       Time - O(n)
       Space - O(n)

       Runtime:
       90 / 90 test cases passed.
           Status: Accepted
       Runtime: 728 ms
       Memory Usage: 20.2 MB
       """

    def totalFruit(self, fruits: List[int]) -> int:
        fruitCount, left = {}, 0

        for right, currFruit in enumerate(fruits):
            fruitCount[currFruit] = fruitCount.get(currFruit, 0) + 1

            if len(fruitCount) > 2:
                fruitCount[fruits[left]] -= 1

                if fruitCount[fruits[left]] == 0:
                    del fruitCount[fruits[left]]

                left += 1

        return right - left + 1

    """
    Solution technique: two pointer using Counter / Dict to store freq count of each fruit

    Time & Space Complexity:
    Time - O(n^2) ?
    Space - O(1), since at most there will only be three fruits in the basket

    Runtime:
     90 / 90 test cases passed.
            Status: Accepted
        Runtime: 900 ms
        Memory Usage: 20.1 MB """

    # def totalFruit(self, fruits: List[int]) -> int:
    #     l, nums, res = 0, Counter(), 0
    #     for r in range(len(fruits)):
    #         nums[fruits[r]] += 1
    #         while len(nums) > 2:
    #             nums[fruits[l]] -= 1
    #             if not nums[fruits[l]]:
    #                 nums.pop(fruits[l])
    #             l += 1
    #         res = max(res, r - l + 1)
    #     return res


myobj = Solution()
# inpt = [0, 1, 6, 6, 4, 4, 6]
# op = 5
# inpt = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
# # op = 5

inpt = [1, 0, 1, 4, 1, 4, 1, 2, 3]
# op = 5
print(myobj.totalFruit(inpt))

"""
import file_name
def test_name():
    assert file_name.Solution().functionName(val) == OP
"""
