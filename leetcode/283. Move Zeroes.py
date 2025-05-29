from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left] != 0:
                left += 1
            right += 1
        print(nums)


Solution().moveZeroes([2, 1])
Solution().moveZeroes([1, 0, 1])
