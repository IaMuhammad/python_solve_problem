class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        p1, p2, res = 0, 0, []
        nums1.sort()
        nums2.sort()

        while p1 < len(nums1) and p2 < len(nums2):
            if len(nums2) == p2 and len(nums1) == p1:
                break
            elif nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 = min(p1+1, len(nums1))
            else:
                p2 = min(p2+1, len(nums2))
        return res


a = Solution()
print(a.intersect([1,2,3], [1,2,3]))