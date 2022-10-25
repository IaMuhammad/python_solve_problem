def bin_pow(a, n):
    if n == 1:
        return a
    s = bin_pow(a, n//2)
    if n & 1:
        return a * s * s
    return s * s