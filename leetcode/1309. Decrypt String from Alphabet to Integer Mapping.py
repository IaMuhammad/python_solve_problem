def freqAlphabets(s: str) -> str:
    ans = ''
    l = len(s)-1
    while l>=0:
        if s[l] == '#':

            ans = chr(96 + int(s[l-2:l])) + ans
            l -= 2
        else:
            ans = chr(96 + int(s[l])) + ans
        l -= 1
    return ans
print(freqAlphabets('10#11#12'))