def is_sorted(l):
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            return False
    return True
def minDeletionSize(strs: list[str]) -> int:
    strs = [[j for j in i] for i in strs]
    c = 0
    for i in zip(*strs):
        if not is_sorted(''.join(i)):
            c += 1
    return c


print(minDeletionSize(['salom', 'salom']))