from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            res = nums.index(target)
            return res
        else:
            return -1


# example
obj = Solution()
print(obj.search([1,3,5,6,7], 5))
