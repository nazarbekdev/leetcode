from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [''] * len(s)

        for i, index in enumerate(indices):
            shuffled[index] = s[i]

        return ''.join(shuffled)


# example
obj = Solution()
print(obj.restoreString("codeleet", [4, 6, 5, 7, 0, 2, 1, 3]))
