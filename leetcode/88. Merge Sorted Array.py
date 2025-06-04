from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        _nums1 = nums1[:m]
        i = 0
        while _nums1 and nums2:
            if _nums1[0] <= nums2[0]:
                nums1[i] = _nums1.pop(0)
            elif _nums1[0] > nums2[0]:
                nums1[i] = nums2.pop(0)
            else:
                nums1[i] = nums2.pop(0)
            i += 1
        nums1[i:] = _nums1 + nums2
        print(nums1)
a = Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)