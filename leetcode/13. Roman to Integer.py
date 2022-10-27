def romanToInt(s: str):
    d = {
        'I':    1,
        'V':    5,
        'X':    10,
        'L':    50,
        'C':    100,
        'D':    500,
        'M':    1000
    }
    # s = 'XXIV'
    # s = 'V I X X'
    l = summa = 0
    for i in s[::-1]:
        if l > d[i]:
            summa -= d[i]
        else:
            summa += d[i]
        l = d[i]
    return summa

print(romanToInt('XXIV'))