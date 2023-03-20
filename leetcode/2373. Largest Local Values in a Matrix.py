class Solution:
    def max(self, grid_3: list[list[int]], j) -> int:
        return max([max(i[j:j + 3]) for i in grid_3])

    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        matrix = []
        for i in range(len(grid) - 2):
            l = []
            for j in range(len(grid) - 2):
                l.append(self.max(grid[i:i + 3], j))
            matrix.append(l)
        return matrix


a = Solution()
print(a.largestLocal(grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))


def fun(mat, i, j):
    three = mat[i:i + 3]
    ind = 0
    for i in three:
        three[ind] = i[j:j + 3]
        ind += 1

    return maks(three)


def maks(mat):
    m = mat[0][0]
    for i in mat:
        if max(i) > m:
            m = max(i)
    return m


grid = [[9, 9, 8, 1, 10],
        [5, 6, 2, 6, 11],
        [8, 2, 6, 4, 12],
        [6, 2, 2, 2, 13],
        [1, 2, 4, 5, 4]]

n = len(grid) - 2
maxLocal = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]

for i in range(len(grid) - 2):
    for j in range(len(grid) - 2):
        maxLocal[i][j] = fun(grid, i, j)
