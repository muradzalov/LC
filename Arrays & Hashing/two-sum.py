# Link: https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109

# Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# ----------------------------------------------------------------------------------------------------------------------------------
nums = [2, 7, 11, 15]
target = 9

from typing import List
# import time

# class BruteForceSolution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         arrayLength = len(nums)
#         for i in range(arrayLength - 1):
#             for j in range(i + 1, arrayLength):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []


class OptimizedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n): # iterate over array
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []
    
# Time complexity: The `OptimizedSolution` has a time complexity of O(n). This is because it processes each element in the list exactly once. Each lookup in the hash table - to check if the complement exists - is O(1) on average due to the properties of hash tables, making the entire loop run in linear time.
# Space complexity: The space complexity is O(n). In the worst case, the function might end up inserting nearly every element into the hash table if no two numbers sum up to the target early on. Thus, the space required for the hash table grows linearly with the size of the input list.



# print("Brute Force Solution:", BruteForceSolution().twoSum(nums, target))
print("Optimized Solution:", OptimizedSolution().twoSum(nums, target))
