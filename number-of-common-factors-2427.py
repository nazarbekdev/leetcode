class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a_lst = []
        b_lst = []
        count = 0
        for i in range(1, a+1):
            if a % i == 0:
                a_lst.append(i)
        for i in range(1, b+1):
            if b % i == 0:
                b_lst.append(i)
        if len(a_lst) > len(b_lst):
            for num in b_lst:
                if num in a_lst:
                    count += 1
        else:
            for num in a_lst:
                if num in b_lst:
                    count += 1
        return count


# example
obj = Solution()
print(obj.commonFactors(10,4))
