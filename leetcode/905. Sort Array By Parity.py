def sortArrayByParity(nums: list):
    l, r, length = 0, len(nums) - 1, len(nums)
    while l < r:
        while l < length and not (nums[l] & 1):
            l += 1
        if l >= r:
            break
        while r > -1 and nums[r] & 1:
            r -= 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
    return nums
print(sortArrayByParity([0,2]))