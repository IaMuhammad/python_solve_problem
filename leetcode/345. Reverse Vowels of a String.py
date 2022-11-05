def reverseVowels(s: str) -> str:
    l, r, ans = 0, len(s) - 1, ''
    length = len(s)
    d = {
        'a': False,  'e': False,
        'A': False,  'E': False,
        'u': False,  'i': False,
        'U': False,  'I': False,
        'o': False,  'O': False
    }

    while l < len(s):
        while l < length and d.get(s[l], True):
            ans += s[l]
            l += 1
        if l >= length:
            break

        while r >= 0 and d.get(s[r], True):
            r -= 1
        ans += s[r]


        l += 1
        r -= 1

    return ans

print(reverseVowels('aA'))
