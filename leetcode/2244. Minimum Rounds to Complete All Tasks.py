from collections import Counter


def minimumRounds(tasks: list[int]) -> int:
    c = 0
    for k, v in Counter(tasks).items():
        if v == 1:
            return -1
        c += (v+2) // 3
    return c

print(minimumRounds([2,2,3,3,2,4,4,4,4,4]))
"""
2
[,4]
4 // 3
2
"""
