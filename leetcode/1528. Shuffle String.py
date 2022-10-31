def restoreString(s, indices):
    answer = [1, 2]
    answer1 = []
    for item in s:
        answer1.append(item)
    
    answer[0] = indices
    answer[1] = answer1
    
    n = len(answer[0])
    
    for i in range(0, n):
        for j in range(n - 2, i - 1, -1):
            if answer[0][j] > answer[0][j + 1]:
                x = answer[0][j + 1]
                answer[0][j + 1] = answer[0][j] 
                answer[0][j] = x

                x = answer[1][j + 1]
                answer[1][j + 1] = answer[1][j] 
                answer[1][j] = x

    s = ''
    for item in answer[1]:
        s += item

    return s

print(restoreString('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]))