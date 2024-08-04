class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)

        # Define the 32-bit signed integer limits
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # Ensure result is within the 32-bit signed integer range
        if res < INT_MIN:
            return INT_MIN
        elif res > INT_MAX:
            return INT_MAX
        else:
            return res


obj = Solution()
print(obj.divide(dividend=7, divisor=-3))