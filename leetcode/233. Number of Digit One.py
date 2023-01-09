# class Solution:
#     def count(self, n: int):
#         if not n: return 0
#         return self.countDigitOne(n - 1) + f"{n}".count("1")
#
#     def countDigitOne(self, n: int):
#         if n < 100:
#             return self.count(n)
#
#         s = str(n)
#         i = len(s)
#         if set(s) == {'9'}:
#             return i * bin_pow(10, i - 1)
#         if n != int('9' * i):
#             i -= 1
#         _3 = int(f'{s[1:]}') + 1 if int(s[0]) == 1 else bin_pow(10, len(s)-1)
#         return i * bin_pow(10, i - 1) * int(s[0]) + _3 + self.countDigitOne(int(s[1:]))

class Solution:
    def countDigitOne(self, n: int) -> int:
        k, mulk = 0, 1
        res = 0
        while n >= mulk:
            res += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            k += 1
            mulk *= 10
        return res

def bin_pow(a, n):
    if n <= 1:
        return [1, a][n == 1]
    s = bin_pow(a, n // 2)
    if n & 1:
        return a * s * s
    return s * s

a = Solution()
print(a.countDigitOne(1121))