from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            arr[i] = max_value
            max_value = max(max_value, val)
        return arr

a = Solution()
print(a.replaceElements([17, 18, 5, 4, 6, 1]))
