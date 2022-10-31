def addBinary(a, b):
    c = int(str(a), 2) + int(str(b), 2)
    answer = str(bin(c))
    answer = answer[2:]
    return str(answer)

print(addBinary(1010, 1011))