from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i, numm in enumerate(nums):
            if target-numm in data:
                return [data[target-numm], i]
            else:
                data[numm] = i

a = Solution()
print(a.twoSum([2, 7, 11, 15], 9))