def maxSum(grid: list[list[int]]) -> int:
    def hourglass(mat):
        return (sum(mat[0]) + sum(mat[2]) + mat[1][1])

    l1 = len(grid)
    l2 = len(grid[0])
    s = 0
    for i in range(l1 - 2):
        for j in range(l2 - 2):
            k = hourglass([grid[i][j:j + 3], grid[i + 1][j:j + 3], grid[i + 2][j:j + 3]])
            if s < k:
                s = k
    return s

print(maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]))