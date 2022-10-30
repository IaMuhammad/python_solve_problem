def findTheWinner(n: int, k: int) -> int:
    list1 = [_ + 1 for _ in range(n)]
    ind = k - 1
    while len(list1) != 1:
        list1.pop(ind)
        ind += k - 1
        if ind >= len(list1):
            ind %= len(list1)

    return list1[0]

print(findTheWinner(5, 2))