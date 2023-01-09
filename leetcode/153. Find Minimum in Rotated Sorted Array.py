class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[0] and nums[m - 1] >= nums[0]:
                return nums[m]
            elif nums[m] < nums[0]:
                r = m - 1
            else:
                l = m + 1


a = Solution()
print(a.findMin([2, 1]))
