from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer, prev = 0, -101
        for i in range(len(nums)):
            if prev != nums[i]:
                nums[answer] = nums[i]
                answer += 1
            prev = nums[i]
        return answer


print(Solution().removeDuplicates([1, 1, 2]))
