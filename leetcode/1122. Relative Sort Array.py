from collections import Counter


def del_spec(l: list, n: int):

    pass

def relativeSortArray(arr1, arr2):
    dic = Counter(arr1)
    dic2 = Counter(arr2)
    res = []
    for i in arr2:
        res += [i] * dic[i]

    for i in arr1:
        if dic2.get(i):
            pass
        else:
            res += [i]

    return res

print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))