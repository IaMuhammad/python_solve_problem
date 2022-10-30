def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
    res = []
    for i in image:
        l = []
        for j in i[::-1]:
            l.append(int(not (j)))
        res.append(l)
    return res

print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))