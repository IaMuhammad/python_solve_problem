from string import ascii_lowercase


class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        d = {}
        for i, v in enumerate(s):
            if d.get(v, False):
                d[v] = (i - int(d[v][0]) - 1, ord(v) - 97)
            else:
                d[v] = (i,)
        for i, v in d.items():
            if v[0] != distance[v[1]]:
                return False
        return True

a = Solution()
print(
    a.checkDistances('abaccb', distance=[1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))