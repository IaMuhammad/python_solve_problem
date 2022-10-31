def cellsInRange(s):
    a1 = s[0]
    n1 = int(s[1])
    a2 = s[3]
    n2 = int(s[4])
    answer = []

    if n1 != 1:
        for i in range(ord(a1), ord(a2) + 1):
            for j in range(n1, n2 + 1):
                answer.append(chr(i) + str(j))
    else:
        for i in range(ord(a1), ord(a2) + 1):
            for j in range(1, n2 + 1):
                answer.append(chr(i) + str(j))

    
    
    return answer

print(cellsInRange('U6:X9'))