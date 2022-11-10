from collections import Counter


def areOccurrencesEqual(s: str):
    return len(set(Counter(s).values())) == 1
print(areOccurrencesEqual('abcacb'))