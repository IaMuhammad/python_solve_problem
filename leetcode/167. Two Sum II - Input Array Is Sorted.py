from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        data = {}
        for i, v in enumerate(numbers, 1):
            if data.get(target - v):
                return [data.get(target - v), i]
            data[v] = i


a = Solution().twoSum([2, 7, 11, 15], 9)
print(a)  # Output: [1, 2]
