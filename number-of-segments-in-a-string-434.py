class Solution:
    def countSegments(self, s: str) -> int:
        strip_str = s.strip()
        words = strip_str.split()
        return len(words)


# example
obj = Solution()
print(obj.countSegments("hello world"))
