from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         zero_ctr = 0
#         v1 = 1
#         v2 = 1
#         for i in nums:
#             if i == 0:
#                 zero_ctr +=1
#                 v1 *= i
#                 continue
#             v1 *= i
#             v2 *= i
#         if zero_ctr > 1:
#             return [0]*len(nums)
#         elif zero_ctr == 1:
#             for i in range(len(nums)):
#                 if nums[i] != 0:
#                     nums[i] = v1 // nums[i]
#                 else:
#                     nums[i] = v2
#             return nums
#         else:
#             for i in range(len(nums)):
#                 nums[i] = v1 // nums[i]
#             return nums

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplied_val, zero_counter = 1, 0
        for i in nums:
            if i == 0:
                zero_counter += 1
            else:
                multiplied_val *= i
        if zero_counter > 1:
            return [0] * len(nums)
        elif zero_counter == 1:
            return [0 if i != 0 else multiplied_val for i in nums]
        return [int(multiplied_val / i) for i in nums]


a = Solution()

print(a.productExceptSelf([0, 2, 3, 4]))

# def multiply_recursion(l1):
#     if len(l1) == 1:
#         return l1
#     value = multiply_recursion(l1[1:])
#     l1[0] = l1[0] * value[0]
#     l1[1:] = value
#     return l1
#
#
# print(multiply_recursion([5, 2, 3, 4]))
