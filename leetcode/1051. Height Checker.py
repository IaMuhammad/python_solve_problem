def heightChecker(heights):
    heights_sort = sorted(heights)
    c = 0
    for i in zip(heights, heights_sort):
        if i[0] != i[1]:
            c += 1
    return c
print(heightChecker([1,1,4,2,1,3,5]))