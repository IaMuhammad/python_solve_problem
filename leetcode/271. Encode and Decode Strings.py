from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return str(strs)

    def decode(self, s: str) -> List[str]:
        return list(s)


a = Solution()
coded = a.encode(["neet", "code", "love", "you"])
print(coded)
print(a.decode(coded))
