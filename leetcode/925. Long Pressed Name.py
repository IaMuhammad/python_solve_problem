def isLongPressedName(name: str, typed: str) -> bool:
    l1, c1, l2, c2 = 0, 0, 0, 0
    length1, length2 = len(name), len(typed)
    cache = name[0]
    cashe = ''
    while l1 < length1 and l2 < length2:
        if name[l1] == typed[l2]:
            cache = name[l1]
            l1 += 1
            l2 += 1
        elif typed[l2] == cache:
            l2 += 1
        else:
            return False
    print(set(typed[l2:]), set(cache))
    if set(typed[l2:]) == set(cache):
        return True
    elif typed[l2:] or name[l1:]:
        return False
    return True

print(isLongPressedName("vtkgn", "vttkgnn"))