from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if not c:
            return True
        for i in range(1, (c+1) // 2 + 1):
            try:
                if sqrt(c - i * i).is_integer():
                    return True
            except:
                break
            print(i)
        return False

a = Solution()
print(a.judgeSquareSum(999999999))