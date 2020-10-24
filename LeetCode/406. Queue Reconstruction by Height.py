from typing import List

"""
Problem Name: 406. Queue Reconstruction by Height

Problem URL: https://leetcode.com/problems/queue-reconstruction-by-height/

Problem Section: 

Problem Statement:
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
 

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


Resources:
https://leetcode.com/problems/queue-reconstruction-by-height/discuss/167308/Python-solution
https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort%2BInsert-solution

runtime: 
37 / 37 test cases passed.
	Status: Accepted
Runtime: 88 ms
Memory Usage: 14.6 MB
"""

# Solution techniques are

# Time complexity : O(n2) Space complexity : O(n)


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


myobj = Solution()
inpt = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(myobj.reconstructQueue(inpt))

"""
[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
7 - 0, 1
4 - 4
5 - 0, 2
6 - 1

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""