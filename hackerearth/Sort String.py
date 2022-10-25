def func(s):
    l, r, c = 0, len(s)-1, 0
    while l <= r:
        if s[l] != '0' and '1' != s[r]:
            c += 1
            l += 1
            r -= 1
            continue
        if s[l] == '0':
            l += 1
        if s[r] == '1':
            r -= 1
    print(c)

n = int(input())
ans = []
for i in range(n):
    input()
    ans.append(input())

for i in ans:
    func(i)

"""
0101010101110
0001010101111
0000010111111
0000001111111

10 13


0011100
3 7
"""