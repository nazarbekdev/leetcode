from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            if i < n:
                stack.append(i)

        return result


# example
obj = Solution()
print(obj.nextGreaterElements(nums=[1,5,3,6,8]))
#                                 [-1 ,5, 5, 5, 5]


"""Error solution"""
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         max_num = max(nums)
#         max_indx = nums.index(max_num)
#         nums = nums + [0]
#         for i in range(len(nums)-1):
#             if nums[i] == max_num:
#                 nums[i] = -1
#             elif nums[i] < nums[i+1] and i > max_indx:
#                 nums[i] = nums[i+1]
#             elif nums[i] > nums[i+1] and i > max_indx:
#                 nums[i] = nums[i]+1
#             # elif nums[i] < nums[i+1] and i < max_indx:
#             #     nums[i] = nums[i-1]
#         return nums[:len(nums)-1]
