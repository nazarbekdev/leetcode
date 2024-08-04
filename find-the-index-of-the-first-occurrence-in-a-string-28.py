class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)

        if n == 0:
            return 0

        for i in range(h - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1


obj = Solution()
print(obj.strStr("hello", "ll"))