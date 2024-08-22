class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow_num = 1
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        while n:
            if n % 2:
                pow_num *= x
            x *= x
            n //= 2

        return pow_num


# example
obj = Solution()
print(obj.myPow(2, 30))
