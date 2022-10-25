def mergeSimilarItems(items1, items2):
    d = {}

    for i in items1:
        d[i[0]] = i[1]

    for i in items2:
        if d.get(i[0]):
            d[i[0]] += i[1]
        else:
            d[i[0]] = i[1]
    k = sorted(d.keys())
    res = []
    for i in k:
        res.append([i, d[i]])
    return res

print(mergeSimilarItems([[5,1],[4,2],[3,3],[2,4],[1,5]], [[7,1],[6,2],[5,3],[4,4]]))