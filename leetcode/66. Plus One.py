def plusOne(digits):
    i = 0
    l = len(digits)
    s = ''
    while i < l:
        s = str(digits[l-1]) + s
        l -= 1
    
    s = str(int(s) + 1)
    l = len(s)
    print(f's={s} l = {l}', type(s))
    digits = []
    while i < l:
        digits.append(s[i])
        i += 1
    
    return digits
print(plusOne([9]))