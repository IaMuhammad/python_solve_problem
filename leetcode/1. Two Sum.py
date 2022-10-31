def twoSum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i, v in enumerate(nums):
        if d.get(target-v, -1) != -1:
            return [d[target-v], i]
        d[v] = i
print(twoSum([2,7,11,15], 9))
