from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]):
        new_strs = []
        for i in range(len(strs[0])):
            s = ''
            for j in range(len(strs)):
                s += strs[j][i]
            new_strs.append(s)
        res_count = 0
        for elem in new_strs:
            s = ''
            for j in sorted(elem):
                s += j
            if elem != s:
                res_count += 1
        return res_count


# example
obj = Solution()
print(obj.minDeletionSize(["rrjk","furt","guzm"]))
