from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lst = []
        ln = len(nums)
        for i in range(1, ln):
            minn = nums[0]
            if nums[i] > minn:
                lst.append(nums[i])
            else:
                minn = nums[i]
        return lst, minn


# example
obj = Solution()
print(obj.sortArray([3, 0, 2, 1]))

# in progress
