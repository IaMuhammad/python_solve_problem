class Solution:
    def first_position(self, nums: list[int], target: int):
        l, r = 0, len(nums)-1
        while l < r:
            m = (r + l) // 2
            if nums[m] == target:
                r = m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [-1, l][nums[l] == target]


    def last_position(self, nums: list[int], target: int):

        l, r = 0, len(nums) - 1
        while l < r:
            m = (r + l+1) // 2
            if nums[m] == target:
                l = m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [-1, r][nums[r] == target]

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        return [self.first_position(nums, target), self.last_position(nums, target)]

a = Solution()
print(a.searchRange([], 6))