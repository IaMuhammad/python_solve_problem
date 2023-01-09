class Solution:
    def binary_search(self, arr: list, target: int):
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        # return f'{target} bunday son massivda mavjud emas!'
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target and target <= matrix[m][-1]:
                return self.binary_search(matrix[m], target)
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        return False
a = Solution()
print(a.searchMatrix([[1,3]], 3))