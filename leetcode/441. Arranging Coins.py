class Solution:
    def bin_pow(self, a, n):
        if not n:
            return 1
        if n == 1:
            return a
        s = self.bin_pow(a, n // 2)
        if n & 1:
            return a * s * s
        return s * s

    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        l, r = 0, n // 2
        while l <= r:
            m = (l + r) // 2
            k = self.bin_pow(2, m)
            if k == n:
                return m
            if k < n and k * 2 > n:
                return m+1

            elif k > n:
                r = m - 1
            else:
                l = m + 1

a = Solution()
print(a.arrangeCoins(5))