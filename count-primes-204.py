class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)


# example
obj = Solution()
print(obj.countPrimes(2))


"""Time limit"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if 0 <= n < 3:
            return 0
        count = 0
        for num in range(2, n):
            if all(num % i != 0 for i in range(2, num//2+1)):
                count += 1
        return count


# example
obj = Solution()
print(obj.countPrimes(2))
