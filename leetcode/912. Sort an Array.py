# def sortArray(nums: list) -> list:
#     m = len(nums) // 2
#     if m == 0:
#         return nums
#     L = sortArray(nums[:m])
#     R = sortArray(nums[m:])
#
#     res = []
#     while L and R:
#         res.append([R, L][L[0] < R[0]].pop(0))
#     res += L + R
#     # for _ in range(min(len(L), len(R)) * 2):
#     #     res = [[R, L][L[0] < R[0]].pop(0)]
#     return res
#
# print(sortArray([5,2,3,1,4]))


class Solution:
    def sortArray(self, nums):
        if len(nums) == 1:
            return nums
        left = self.sortArray(nums[:len(nums) // 2])
        right = self.sortArray(nums[len(nums) // 2:])

        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged += left + right
        return merged

a = Solution()


print(a.sortArray([5, 2, 3, 1]))
