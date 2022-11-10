def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i-1][j-1] != matrix[i][j]:
                return False
    return True