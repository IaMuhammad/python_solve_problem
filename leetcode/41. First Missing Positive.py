def firstMissingPositive(nums: list[int]) -> int:
    d, i = {}, 1
    for ind in nums:
        d[ind] = True
    while d.get(i, False):
        i += 1
    return i
print(firstMissingPositive([7,8,9,11,12]))