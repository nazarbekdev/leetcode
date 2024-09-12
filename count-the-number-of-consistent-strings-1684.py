from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        result = 0

        for word in words:
            if all(char in allowed_set for char in word):
                result += 1

        return result


# example
obj = Solution()
print(obj.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
