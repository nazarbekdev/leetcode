from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res_lst = []
        for i in range(1, len(nums) + 1):
            res_lst.append(sum(nums[:i]))
        return res_lst


# example
obj = Solution()
print(obj.runningSum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
