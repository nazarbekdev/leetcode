from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        overal = nums1 + nums2
        overal_sorted = sorted(overal)
        ln = len(overal_sorted)
        if ln == 1:
            return float(overal_sorted[0])
        elif ln % 2 == 1:
            return float(overal_sorted[ln // 2])
        else:
            median = overal_sorted[ln // 2 - 1] + overal_sorted[ln // 2]
            return median / 2


# example
obj = Solution()
print(obj.findMedianSortedArrays([1, 3], [2]))
