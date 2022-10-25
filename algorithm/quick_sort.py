from random import randrange


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    m = arr.pop(randrange(len(arr)))
    l = quick_sort([i for i in arr if i <= m])
    r = quick_sort([i for i in arr if i > m])

    return l + [m] + r

print(quick_sort([1,4,6,1,2,8,2]))