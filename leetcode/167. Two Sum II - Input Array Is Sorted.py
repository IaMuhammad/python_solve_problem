class Solution:
    def binary_search(self, arr: list, target: int, l: int):
        r = len(arr)-1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return m + 1
            elif arr[m] > target:
                r = m - 1
            else:
                l = m + 1
        return 0

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i, v in enumerate(numbers):
            b = self.binary_search(numbers, target - v, i + 1)
            if b:
                return [i+1, b]


a = Solution()
print(a.twoSum([5,25,75],100))
