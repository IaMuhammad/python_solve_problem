def intToRoman(num: int):
    d = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    s = ''
    # while num:
    for k, v in d.items():
        s += num // v * k
        num %= v

    return s

print(intToRoman(1994))
"""
14
XIIII

40
350
CCCL
"""