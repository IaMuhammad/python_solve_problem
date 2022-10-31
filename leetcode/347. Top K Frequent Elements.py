from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    counter = Counter(nums)
    l = []
    for i in counter.items():
        l.append(list(i))
    l.sort(key=lambda x:x[1], reverse=True)
    return [i[0] for i in l][:k]
print(topKFrequent([1,1,1,2,2,3], 2))