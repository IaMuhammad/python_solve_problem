# # def merge_sort(arr):
# #     if len(arr) == 1:
# #         return arr
# #     m = len(arr) // 2
# #     l = merge_sort(arr[:m])
# #     r = merge_sort(arr[m:])
# #
# #     mr = []
# #     while l and r:
# #         if l[0] < r[0]:
# #             mr.append(l[0])
# #             l.pop(0)
# #         else:
# #             mr.append(r[0])
# #             r.pop(0)
# #     mr += l + r
# #     return mr
# #
# #
# # print(merge_sort([1,4,1,2,6,9,3]))
#
# l1 = [2,5,8,12,16]
# l2 = [3,4,5,7,8,9,10]
#
# mr = []
# while l1 and l2:
#     if l1 < l2:
#         mr.append(l1.pop(0))
#     else:
#         mr.append(l2.pop(0))
#
#
# mr += l1 + l2
# print(mr)

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        L = merge_sort(arr[:mid])
        R = merge_sort(arr[mid:])

        mr = [[R, L][L[0] < R[0]].pop(0) for _ in range(min(len(L), len(R)) * 2)] + L + R

        return mr
    else:
        return arr
print(merge_sort([1,5,2,8,0,3]))