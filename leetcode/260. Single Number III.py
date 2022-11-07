# # def singleNumber(nums: list) -> list:
# #     a = []
# #     for i in nums:
# #         if i in a:
# #             a.remove(i)
# #         else:
# #             a.append(i)
# #     return a
# # print(singleNumber([1,2,1,3,2,5]))
#
# def solve(nums: int):
#     diff, result = 0, [0, 0]
#     for i in nums:
#         diff ^= i
#     k = 0 ^ 3 ^ 5
#     diff &= -diff
#     for num in nums:
#         if num & diff == 0:
#             result[0] ^= num
#         else:
#             result[1] ^= num
#     return result
# print(solve([1,2,1,4,8,4,10,8,2,12]))
# print(0^3^5)
# print(32&2)
for i in range(1, 51):
    print(i, i & 8)