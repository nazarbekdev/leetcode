class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        if len(word) < 2:
            return True
        if word[0].isupper() and word[1].isupper():
            for i in word[1:]:
                if i.isupper():
                    count += 1
            if count == len(word[1:]):
                return True
            else:
                return False
        if word[0].isupper():
            for i in word[1:]:
                if i.islower():
                    count += 1
            if count == len(word[1:]):
                return True
            else:
                return False
        elif word[0].islower():
            for i in word[1:]:
                if i.islower():
                    count += 1
            if count == len(word[1:]):
                return True
            else:
                return False


obj = Solution()
print(obj.detectCapitalUse("B"))