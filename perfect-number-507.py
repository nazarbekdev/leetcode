import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        summ = 1
        sqrt_num = int(math.sqrt(num))

        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                summ += i
                if i != num // i:
                    summ += num // i

        return summ == num


# example
obj = Solution()
print(obj.checkPerfectNumber(99999992))
