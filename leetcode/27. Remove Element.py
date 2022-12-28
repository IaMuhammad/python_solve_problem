class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        l = c = 0
        r = len(nums) - 1
        while l < r:
            try:
                while nums[l] != val:
                    l += 1
            except:
                pass
            while nums[r] == val and r:
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                c += 1

        print(nums)
        return r + [1, 0][nums[r] == val]

a = Solution()
# print(a.removeElement([2, 2], 3))
# print(a.removeElement([3,2,2,3], 3))
# print(a.removeElement([0,1,2,2,3,0,4,2], 2))
print(a.removeElement([], 2))
