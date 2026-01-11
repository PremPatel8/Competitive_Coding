"""
[1899. Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) A **triplet** is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [ai, bi, ci]` describes the `ith` **triplet**. You are also given an integer array `target = [x, y, z]` that describes the **triplet** you want to obtain.
 
To obtain `target`, you may apply the following operation on `triplets` **any number** of times (possibly **zero**):
 
- Choose two indices (**0-indexed**) `i` and `j` (`i != j`) and **update** `triplets[j]` to become `[max(ai, aj), max(bi, bj), max(ci, cj)]`.- For example, if `triplets[i] = [2, 5, 3]` and `triplets[j] = [1, 7, 5]`, `triplets[j]` will be updated to `[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]`.
 
Return `true`  *if it is possible to obtain the* `target` ***triplet*** `[x, y, z]` *as an** element** of* `triplets` *, or* `false` *otherwise* .
 
**Example 1:**
**Input:** triplets = `[2, 5,3],[1,8,4],[1,7,5]`, target = [2,7,5]
**Output:** true
**Explanation:** Perform the following operations:
- Choose the first and last triplets `[2, 5,3],[1,8,4],[1,7,5]`. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = `[2, 5,3],[1,8,4],[2,7,5]`
The target triplet [2,7,5] is now an element of triplets.
 
**Example 2:**
**Input:** triplets = `[3, 4,5],[4,5,6]`, target = [3,2,5]
**Output:** false
**Explanation:** It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.
 
**Example 3:**
**Input:** triplets = `[2, 5,3],[2,3,4],[1,2,5],[5,2,3]`, target = [5,5,5]
**Output:** true
**Explanation: **Perform the following operations:
- Choose the first and third triplets `[2, 5,3],[2,3,4],[1,2,5],[5,2,3]`. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = `[2, 5,3],[2,3,4],[2,5,5],[5,2,3]`.
- Choose the third and fourth triplets `[2, 5,3],[2,3,4],[2,5,5],[5,2,3]`. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = `[2, 5,3],[2,3,4],[2,5,5],[5,5,5]`.
The target triplet [5,5,5] is now an element of triplets.
 
**Constraints:**
 
- `1 <= triplets.length <= 105`
- `triplets[i].length == target.length == 3`
- `1 <= ai, bi, ci, x, y, z <= 1000`
"""

"""
Greedy Set Approach: Track Valid Target Indices

Time complexity: O(n), where n is the number of triplets in the array. We iterate through each triplet once.
Space complexity: O(1) - We use a set with a maximum size of 3 to store the indices of matching elements. Therefore, the space complexity is constant.
"""
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = set()  # Initialize a set to store indices of matching elements
        
        # Iterate through each triplet
        for triplet in triplets:
            # If any element of the triplet is greater than the corresponding element of the target triplet, skip
            if any(t > tgt for t, tgt in zip(triplet, target)):
                continue
            
            # Check if any element of the triplet matches the corresponding element of the target triplet
            # Add matching indices to the set
            for i, (v, tgt) in enumerate(zip(triplet, target)):
                if v == tgt:
                    ans.add(i)
            
            # Early termination: if all 3 positions are found, return immediately
            if len(ans) == 3:
                return True
        
        # Check if all three indices are present in the set
        return len(ans) == 3