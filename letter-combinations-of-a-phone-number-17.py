from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chrs = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        res = []
        if len(digits) == 0:
            return res
        if len(digits) == 1:
            return chrs[digits]
        if len(digits) == 2:
            for i in chrs[digits[0]]:
                for j in chrs[digits[1]]:
                    s = i + j
                    res.append(s)
        if len(digits) == 3:
            for i in chrs[digits[0]]:
                for j in chrs[digits[1]]:
                    for k in chrs[digits[2]]:
                        s = i + j + k
                        res.append(s)
        if len(digits) == 4:
            for i in chrs[digits[0]]:
                for j in chrs[digits[1]]:
                    for k in chrs[digits[2]]:
                        for l in chrs[digits[3]]:
                            s = i + j + k + l
                            res.append(s)
        return res


# example
obj = Solution()
print(obj.letterCombinations("23"))
