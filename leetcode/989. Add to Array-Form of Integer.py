def addToArrayForm(num, k):
    i = 0
    l = len(num)
    s = ''
    while i < l:
        s = str(num[l-1]) + s
        l -= 1
    
    s = str(int(s) + k)
    l = len(s)
    num = []
    while i < l:
        num.append(s[i])
        i += 1
    
    return num

print(addToArrayForm([1, 5, 8], 90))