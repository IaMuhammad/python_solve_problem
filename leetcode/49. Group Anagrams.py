from collections import Counter
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        data = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in data:
                answer[data[sorted_str]].append(i)
            else:
                data[sorted_str] = len(answer)
                answer.append([i])

        return answer


a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
