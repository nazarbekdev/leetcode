from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums2.sort()

        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            k = bin(mask).count('1')
            for j in range(n):
                if mask & (1 << j) == 0:
                    dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + (nums1[k] ^ nums2[j]))

        return dp[(1 << n) - 1]


# example
obj = Solution()
print(obj.minimumXORSum([72, 97, 8, 32, 15], [63, 97, 57, 60, 83]))
