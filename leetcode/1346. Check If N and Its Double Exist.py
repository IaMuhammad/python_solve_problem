class Solution:
    def binary_search(self, arr: list, target: int):
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                print(arr[m])
                return True
            elif arr[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False

    def checkIfExist(self, arr: list[int]) -> bool:
        arr.sort()
        for i, v in enumerate(arr):
            if self.binary_search(arr[:i] + arr[i+1:], v * 2) or self.binary_search(arr[:i] + arr[i+1:], v / 2):
                return True
        return False


a = Solution()
print(a.checkIfExist([-2,0,10,-19,4,6,-8]))
