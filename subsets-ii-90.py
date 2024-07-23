from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                subsets_count = len(result)
            for j in range(len(result) - subsets_count, len(result)):
                result.append(result[j] + [nums[i]])

        return result


# example
obj = Solution()
print(obj.subsetsWithDup([1,2,3]))