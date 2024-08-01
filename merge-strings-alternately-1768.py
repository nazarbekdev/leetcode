class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''.join(a + b for a, b in zip(word1, word2))
        longer = word1 if len(word1) > len(word2) else word2
        result += longer[len(result)//2:]
        return result


# example
obj = Solution()
print(obj.mergeAlternately("abc", "pqrs"))
