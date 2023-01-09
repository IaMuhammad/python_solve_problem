class Solution:
    def bsa_count(self, arr: list[int]):
        l, r = 0, len(arr) - 1
        if arr[r]:
            return r + 1
        if not arr[l]:
            return 0
        while l <= r:
            m = (l + r+1) // 2
            if arr[m] == 0:
                if arr[m - 1] == 1:
                    return m
                r = m - 1
            else:
                l = m + 1

    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        l = []
        for i, v in enumerate(mat):
            l.append((self.bsa_count(v),i))

        l.sort()
        print(l)
        return [i[1] for i in l[:k]]


a = Solution()
print(a.kWeakestRows([[1,1,1,1,1],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,0],[1,1,1,1,1]], 3))
