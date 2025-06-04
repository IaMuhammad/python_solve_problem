from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]
        for i in prices[1:]:
            if i < min_value:
                min_value = i
            else:
                _profit = i - min_value
                if _profit > max_profit:
                    max_profit = _profit
        return max_profit


a = Solution().maxProfit([7, 1, 4, 3, 6])
print(a)
