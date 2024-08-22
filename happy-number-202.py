class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        count = 0
        while True:
            n = str(n)
            sm = 0
            for i in n:
                sm += int(i)**2
                count += 1
            n = sm
            if sm == 1:
                happy_num = True
                break
            if count > 20:
                happy_num = False
                break
        return happy_num


# example
obj = Solution()
print(obj.isHappy(7))
