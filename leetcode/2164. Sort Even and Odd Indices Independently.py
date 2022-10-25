def sortEvenOdd(nums):
    odd = []
    even = []
    for i, v in enumerate(nums):
        if i & 1:
            odd.append(v)
        else:
            even.append(v)

    odd.sort(reverse=True)
    even.sort()
    res = []

    for i in even:
        res.append(i)
        if odd:
            res.append(odd.pop(0))

    return res
print(sortEvenOdd([4,1,2,3]))
