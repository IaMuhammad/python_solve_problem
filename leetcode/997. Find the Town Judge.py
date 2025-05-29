from collections import Counter
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        counters = Counter([i[1] for i in trust])
        non_judges = {a:True for a, b in trust}
        _ = -1
        for key, value in counters.items():
            if value == n - 1:
                if _ != key and _ != -1:
                    return -1
                _ = key

        return -1 if non_judges.get(_) else _


