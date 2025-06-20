from typing import List, Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        data = Counter(nums)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if data.get(-1 * (nums[i] + nums[j])):
                    print([nums[i], nums[j], -1 * (nums[i] + nums[j])])
                    answer.append([nums[i], nums[j], -1 * (nums[i] + nums[j])])
        return answer


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
