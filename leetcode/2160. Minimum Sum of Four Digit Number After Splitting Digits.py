def minimumSum(num):

    n = []
    n.append(num % 10)
    num //= 10
    n.append(num % 10)
    num //= 10
    n.append(num % 10)
    num //= 10
    n.append(num % 10)
    num //= 10
    
    a = []
    a.append(min(n))
    n.remove(min(n))

    a.append(max(n))
    n.remove(max(n))

    a.append(min(n))
    a.append(max(n))


    return a[0] * 10 + a[1] + a[2] * 10 + a[3]


print(minimumSum(2932))