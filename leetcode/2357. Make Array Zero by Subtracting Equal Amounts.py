def minimumOperations(nums):
    nums = set(nums)
    if 0 in nums:
        return len(nums) - 1
    return len(nums)
    return nums
print(minimumOperations([1,5,0,3,5]))