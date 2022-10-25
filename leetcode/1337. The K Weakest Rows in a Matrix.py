def kWeakestRows(mat, k):
    r = []
    for i, v in enumerate(mat):
        r.append([v.count(1), i])
    r.sort()
    r = [i[1] for i in r]
    
    return r[:k]

print(kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))