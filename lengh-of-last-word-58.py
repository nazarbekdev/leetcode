class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip(' ')
        words = words.split(' ')
        return len(words[-1])


# example
obj = Solution()
print(obj.lengthOfLastWord('   fly me   to   the moon  '))
