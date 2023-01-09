class Solution:
    def is_left(self, n: int, arr: list[int], d: int):
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l + r) // 2
            if abs(arr[m] - n) <= d:
                return True
            elif arr[m] > n:
                r = m - 1
            else:
                l = m + 1
        return False

    def is_right(self, n: int, arr: list[int], d: int):
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l + r) // 2
            if abs(arr[m] - n) <= d:
                return True
            elif arr[m] < n:
                r = m - 1
            else:
                l = m + 1
        return False

    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        c = 0
        for i in arr1:
            if not self.is_left(i, arr2, d):
                if not self.is_right(i, arr2, d):
                    print(i)
                    c += 1
        return c


a = Solution()
print(a.findTheDistanceValue(arr1=[1,4,3], arr2=[-4,-3,6,10,20,30], d=3))
