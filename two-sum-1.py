from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        if nums[0] + nums[1] == target:
            return [0, 1]
        for i in range(ln):
            num1 = nums[i]
            for j in range(i + 1, ln):
                if num1 + nums[j] == target:
                    return [i, j]


# example
obj = Solution()
print(obj.twoSum(
    [3, 2, 3], 6))
