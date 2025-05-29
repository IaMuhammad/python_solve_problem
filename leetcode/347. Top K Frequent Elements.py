from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        return [x[0] for x in counted.most_common(k)]


nums = [1, 3]
print(Solution().topKFrequent(nums, 2))
