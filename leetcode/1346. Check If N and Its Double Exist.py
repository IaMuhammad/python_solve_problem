def checkIfExist(arr: list) -> bool:
    d = {}
    for i in arr:
        if d.get(i*2, False) or d.get(i/2, False):
            return True
        else:
            d[i] = True
    return False