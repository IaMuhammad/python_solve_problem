def islandPerimeter(grid: list[list[int]]) -> int:
    ans = 0
    l = {}
    for i in grid:
        _ = {}
        ex_ind = -3
        for ind, j in enumerate(i):
            if j and l.get(ind, 0):
                ans -= 2
            if j and ind - ex_ind == 1:
                ans -= 2
            if j:
                ans += 4
                _[ind] = 1
                ex_ind = ind
        l = _
    return ans
print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))