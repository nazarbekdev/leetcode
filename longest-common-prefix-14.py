from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        frst = strs[0]

        for i in strs[1:]:
            index = 0
            while index < len(frst) and index < len(i) and frst[index] == i[index]:
                index += 1

            frst = frst[:index]

            if frst == '':
                break
        return frst


# example
obj = Solution()
print(obj.longestCommonPrefix(["flower", "flow", "flight"]))
