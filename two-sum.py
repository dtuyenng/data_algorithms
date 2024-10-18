"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

from typing import List

nums = [12, -7, 23, -1, 0, 45, -34, 18, 3, -9, 27, -15, 22, 5, -8, 14, -2, 30, -21, 8, -16, 10, 6, -4, 19, -11, 13, -3, 32, -6, 9, -18, 20, -25]
target = 99999

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for index1 in range(0, len(nums)):
#             for index2 in range(0, len(nums)):
#                 print(f"{nums[index1]} + {nums[index2]}")


# Since this is a loop with n item with another lool of n item, the time complexity is
# 0(n^2)

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     index1 = 0
    #     for num in range(0, len(nums)):
    #         index2 = 0
    #         for num in range(0, len(nums)):
    #             # print(f"{index1} | {index2}")
    #             print(f"{nums[index1]} + {nums[index2]} = {nums[index1] + nums[index2]} [{index1},{index2}]")
    #             if index1 != index2:
    #                 print(f"{nums[index1]} + {nums[index2]} = {nums[index1] + nums[index2]} [{index1},{index2}]")
    #                 # return [index1, index2]
    #             index2 += 1
    #         index1 += 1

    # To improve it, try to have the pointer at different end of the list and when they meet, break out


    # def twoSum2(self, nums: List[int], target: int) -> List[int]:
    #     index1 = 0
    #     for num in range(0, len(nums)):
    #         index2 = len(nums) - 1
    #         for num in range(0, len(nums)):
    #             # print(f"{index1} | {index2}")
    #             # if index1 != index2:
    #             if index1 != index2:
    #                 print(f"{nums[index1]} + {nums[index2]} = {nums[index1] + nums[index2]} [{index1},{index2}]")
    #                 if nums[index1] + nums[index2] == target:
    #                     # print(f"[{index1},{index2}]")
    #                     # return [index1, index2]
    #                     pass
    #             elif index1 == index2:
    #                 break
    #             index2 -= 1
    #         index1 += 1

    # def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
    #     access = 0
    #     index1 = 0
    #     hash_table = {}
    #     for num in range(0, len(nums)):
    #         index2 = len(nums) - 1
    #         for num in range(0, len(nums)):
    #             # if hash_table.get((index1, index2), None) is None:
    #             if (hash_table.get((index1, index2), None) is None) or (hash_table.get((index2, index1), None) is None):
    #                 # print(hash_table)
    #                 # print("Not in Hash")
    #                 if index1 != index2:
    #                     # print(f"{nums[index1]} + {nums[index2]} = {nums[index1] + nums[index2]} [{index1},{index2}]")
    #                     sum = nums[index1] + nums[index2]
    #                     hash_table[(index1, index2)] = sum
    #                     # hash_table[(index2, index1)] = sum
    #                     access += 1
    #                     if nums[index1] + nums[index2] == target:
    #                         print(f"Access: {access}")
    #                         return [index1, index2]
    #                 else:
    #                     access += 1
    #             index2 -= 1
    #         index1 += 1
    #     print(f"Access: {access}")
    #
    #
    # def twoSum_nohash(self, nums: List[int], target: int) -> List[int]:
    #     access = 0
    #     index1 = 0
    #     hash_table = {}
    #     for num in range(0, len(nums)):
    #         index2 = len(nums) - 1
    #         for num in range(0, len(nums)):
    #             if index1 != index2:
    #                 # print(f"{nums[index1]} + {nums[index2]} = {nums[index1] + nums[index2]} [{index1},{index2}]")
    #                 hash_table[(index1, index2)] = nums[index1] + nums[index2]
    #                 hash_table[(index2, index1)] = nums[index1] + nums[index2]
    #                 access += 1
    #                 if nums[index1] + nums[index2] == target:
    #                     print(f"Access: {access}")
    #                     return [index1, index2]
    #             else:
    #                 access += 1
    #             index2 -= 1
    #         index1 += 1
    #     print(f"Access: {access}")


    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        access = 0
        index1 = 0
        hash_table = {}
        for num in range(0, len(nums)):
            index2 = len(nums) - 1
            for num in range(0, len(nums)):
                if index1 != index2:
                    if (hash_table.get((index1, index2), None) is None) or (hash_table.get((index2, index1), None) is None):
                        access += 1
                        hash_table[(index1, index2)] = nums[index1] + nums[index2]
                        hash_table[(index2, index1)] = nums[index1] + nums[index2]
                        if nums[index1] + nums[index2] == target:
                            print(f"Access: {access}")
                            return [index1, index2]
                index2 -= 1
            index1 += 1
        print(f"Access: {access}")

    def twoSum_nohash(self, nums: List[int], target: int) -> List[int]:
        access = 0
        index1 = 0
        hash_table = {}
        for num in range(0, len(nums)):
            index2 = len(nums) - 1
            for num in range(0, len(nums)):
                if index1 != index2:
                    access += 1
                    if nums[index1] + nums[index2] == target:
                        print(f"Access: {access}")
                        return [index1, index2]
            index2 -= 1
            index1 += 1
        print(f"Access: {access}")

    def twoSum_gpt(self, nums: List[int], target: int) -> List[int]:
        access = 0
        hash_table = {}

        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):  # Only check each pair once
                sum_value = nums[index1] + nums[index2]
                access += 1  # Increment access for each unique pair checked
                if sum_value not in hash_table:  # Store unique sums only
                    hash_table[(index1, index2)] = sum_value  # Add to hash table
                    if sum_value == target:
                        print(f"Access: {access}")
                        return [index1, index2]

        print(f"Access: {access}")  # Output the total access count


solution = Solution()
print(solution.twoSum_hash(nums, target))
print(solution.twoSum_nohash(nums, target))
print(solution.twoSum_gpt(nums, target))