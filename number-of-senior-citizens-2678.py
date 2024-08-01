from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                count += 1
        return count


# example
obj = Solution()
print(obj.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
