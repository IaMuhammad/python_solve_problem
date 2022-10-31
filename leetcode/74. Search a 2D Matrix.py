def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    index = -1

    if m == 1 and type(matrix[0]) == list and len(matrix[0]) == 1:
        print(5)
        return matrix[0][0] == target

    elif m == 1 and n == 1:
        return matrix == target
    
    for i in range(0, m):
        if matrix[i][n-1] >= target:
            index = i
            break

    left = 0
    right = len(matrix[index]) - 1

    answer = bool()
    for i in range(0, n):
        if matrix[index][i] == target:
            answer = True
    
    return answer

print(searchMatrix([[1], [3]], 1))