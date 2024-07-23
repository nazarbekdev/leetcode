class Solution:
    def intToRoman(self, num: int) -> str:
        ones = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        tens = {0: '', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'}
        hundreds = {0: '', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC',
                    900: 'CM'}
        thousands = {0: '', 1000: 'M', 2000: 'MM', 3000: 'MMM'}

        res = ''

        r1 = num % 10
        r2 = num // 10 % 10 * 10
        r3 = num // 100 % 10 * 100
        r4 = num // 1000 * 1000

        if r4 in thousands.keys():
            res += thousands[r4]
        if r3 in hundreds.keys():
            res += hundreds[r3]
        if r2 in tens.keys():
            res += tens[r2]
        if r1 in ones.keys():
            res += ones[r1]
        return res


# example
obj = Solution()
print(obj.intToRoman(58))
