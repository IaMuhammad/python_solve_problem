def myAtoi(s):
    ans = ''
    s = s.strip()
    if not s:
        return 0
    b = False
    if s[0] == '-':
        b = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    for i in s:
        if i in '0987654321':
            ans += i
        else:
            break
    if ans:
        ans = int(ans)
        if b:
            ans = -1 * ans
            if ans < -2147483648:
                ans = -2147483648
        else:
            if ans > 2147483647:
                ans = 2147483647
        return ans
    else:
        return 0

print(myAtoi("-91283472332"))
