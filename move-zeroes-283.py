from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_lst = []
        res = []
        for i in nums:
            if i == 0:
                zero_lst.append(i)
            else:
                res.append(i)

        for i in range(len(nums)):
            if i < len(res):
                nums[i] = res[i]
            else:
                nums[i] = 0


# example
obj = Solution()
print(obj.moveZeroes([0, 1, 2, 3, 0, 4, 2]))
