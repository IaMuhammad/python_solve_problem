def validPalindrome(s: str) -> bool:
    l, r, c = 0, len(s) - 1, 0
    while l <= r:
        ls, rs = s[l], s[r]
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif not c:
            return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]

    return True
print(validPalindrome("ebcbbececabbacecbbcbe"))
