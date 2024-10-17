class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_letter, upper_letter = [], []
        for letter in word:
            if letter.isupper():
                upper_letter.append(letter.lower())
            elif letter.islower():
                lower_letter.append(letter)
        low_set = set(lower_letter)
        up_set = set(upper_letter)
        count = 0
        if len(low_set) > len(up_set):
            for i in up_set:
                if i in low_set:
                    count += 1
        else:
            for i in low_set:
                if i in up_set:
                    count += 1
        return count


obj = Solution()
word = 'abcAbC'
print(obj.numberOfSpecialChars(word))