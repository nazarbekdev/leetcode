from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = list(sorted(set(nums)))
        print(sorted_nums)
        if len(sorted_nums) < 4:
            return sorted_nums[0]
        else:
            return sorted_nums[-3]


# example
obj = Solution()
print(obj.thirdMax([-1, 2, 3]))
