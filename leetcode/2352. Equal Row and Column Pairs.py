def equalPairs(grid: list[list[int]]) -> int:
    counter = {}
    for i in grid:
        if counter.get(str(i), 0):
            counter[str(i)] += 1
        else:
            counter[str(i)] = 1

    c = 0
    for i in list(map(list, zip(*grid))):
        c += counter.get(str(i), 0)
    return c

print(equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))
"""
3 1 2 2     3 1 2 2     1 4 4 5
1 4 4 4 - > 1 4 4 5 - > 2 4 2 2
2 4 2 2 - > 2 4 2 2 - > 2 4 2 2
2 5 2 2     2 4 2 2     3 1 2 2

"""