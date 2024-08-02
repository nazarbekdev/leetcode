from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        all_sum = ''
        for i in digits:
            all_sum += str(i)
        res = []
        all_int_sum = str(int(all_sum) + 1)
        for i in range(len(all_int_sum)):
            res.append(int(all_int_sum[i]))
        return res


# example
obj = Solution()
print(obj.plusOne([1, 2, 3]))
