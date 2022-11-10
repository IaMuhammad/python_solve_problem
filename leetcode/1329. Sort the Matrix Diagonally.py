def printf(mat):
    for row in mat:
        print(row)

def diagonalSort(mat: list):
    n = len(mat)
    m = len(mat[0])
    for k in range(1, n):
        for i in range(1, n-k+1):
            for j in range(1, m-k+1):
                if mat[i][j] < mat[i-1][j-1]:
                    mat[i][j], mat[i - 1][j - 1] = mat[i-1][j-1], mat[i][j]
    return mat
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
printf(diagonalSort(mat))