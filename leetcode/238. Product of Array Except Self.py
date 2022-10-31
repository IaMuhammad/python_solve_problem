def productExceptSelf(nums: list[int]) -> list[int]:
    s, c, l = 1, 0, 0
    for i in nums:
        if i == 0:
            c += 1
        else:
            s *= i
        l += 1
    if c > 1:
        return [0] * l
    elif c == 1:
        for i in range(l):
            if nums[i] != 0:
                nums[i] = 0
            else:
                nums[i] = s
    else:
        for i in range(l):
            nums[i] = s // nums[i]

    return nums

print(productExceptSelf([1,2,3,4]))