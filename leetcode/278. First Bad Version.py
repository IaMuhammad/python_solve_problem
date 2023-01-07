# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(n):
    return n >= 4

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = c = 0
        while l <= n:
            middle = (l + n) // 2
            if isBadVersion(middle):
                c = middle
                n = middle-1
            else:
                l = middle + 1
        return c
a = Solution()
print(a.firstBadVersion(10))