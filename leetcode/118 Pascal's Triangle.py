from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows+1):
            _ = []
            for j in range(i + 1):
                if j == 0 or i == j:
                    _.append(1)
                else:
                    _.append(answer[-1][j - 1] + answer[-1][j])
            answer.append(_)
        return answer[-1]


a = Solution()
print(a.generate(3))
for i, v in enumerate(a.generate(7)):
    print(i, v)
