def luckyNumbers (matrix):
    ans = []
    x = y = 0
    for row in matrix:
        ans.append([min(row), matrix.index(row), row.index(min(row))])

    x = len(matrix[0])
    y = len(matrix)

    new_mat = []

    for i in range(x):
        l = []
        for j in range(y):
            l.append(matrix[j][i])
        new_mat.append(l)
    
    tr_mat = new_mat

    answer = int()
    for row in ans:
        if row[0] == max(tr_mat[row[2]]):
            return row[0]


print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))