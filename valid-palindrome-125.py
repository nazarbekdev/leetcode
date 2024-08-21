class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold().replace(',', '').replace(' ', '').replace(':', '').replace('.', '').replace('@', '').replace('!', '').replace('$', '').replace('%', '').replace('^', '').replace('&', '').replace('*', '').replace('(', '').replace(')', '').replace('#', '').replace('_', '').replace('-', '').replace('/', '').replace('\\', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('|', '').replace('"', '').replace("'", '').replace('`', '').replace('?', '').replace('<', '').replace('>', '').replace(';', '')
        if len(s) % 2 != 0:
            x = s[:len(s)//2]
            y = s[len(s)//2+1::][::-1]
        else:
            x = s[:len(s) // 2]
            y = s[len(s)//2::][::-1]
        return x == y


# example
obj = Solution()
print(obj.isPalindrome('a.'))
