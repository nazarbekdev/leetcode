class Solution:
    def reverseOnlyLetters(self, s: str):
        letters = [c for c in s if c.isalpha()]

        result = []

        for c in s:
            if c.isalpha():
                result.append(letters.pop())
            else:
                result.append(c)

        return ''.join(result)


# example
obj = Solution()
print(obj.reverseOnlyLetters('a-bC-dEf-ghIj+asd=skd'))
