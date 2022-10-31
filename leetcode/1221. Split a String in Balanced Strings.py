def balancedStringSplit(s):
    ans = ''
    r, l = 0
    c = 0
    for i in s:
        ans+=i
        r = ans.count('R')
        l = ans.count('L')
        if r == l:
            c+=1
            ans = ''
            r, l = 0
    return c