def binary_search_while(arr: list, target: int):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    # return f'{target} bunday son massivda mavjud emas!'
    return -1


def binary_search(arr, target):
    l, r = 0, len(arr)
    m = (l + r) // 2
    if not r:
        return None
    if r == 1:
        return [None, target][arr[0] == target]
    elif arr[m] == target:
        return target
    elif arr[m] > target:
        return binary_search(arr[:m], target)
    return binary_search(arr[m:], target)


def liner_search(arr, target):
    l = len(arr)
    if arr:
        if arr[0] == target:
            return target
        elif l > 1:
            return liner_search(arr[1:], target)
    return None


print(binary_search([-2,0,10,-19,4,6,-8], 22))
