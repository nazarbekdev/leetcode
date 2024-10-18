class Solution:
    def reverseWords(self, s: str) -> str:
        s_splt = s.split(" ")
        reverse_str = ''
        for word in s_splt:
            reverse_str += word[::-1] + ' '
        return reverse_str.strip(' ')


obj = Solution()
print(obj.reverseWords("Hello world"))