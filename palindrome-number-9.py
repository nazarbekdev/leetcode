class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x_ = x[::-1]
        return x == x_


# example
obj = Solution()
print(obj.isPalindrome(121))
