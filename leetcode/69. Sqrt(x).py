class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2
        while l <= r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m < x:
                if (m+1) * (m+1) > x:
                    return m
                l = m+1
            else:
                r = m-1
        return x
a = Solution()
print(a.mySqrt(0))