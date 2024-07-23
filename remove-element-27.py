from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

            j += 1

        return i


# example
obj = Solution()
print(obj.removeElement([3, 2, 2, 3], 2))
