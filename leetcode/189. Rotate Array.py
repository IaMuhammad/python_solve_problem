def rotate(nums, k):
    l = len(nums)
    k = k % l

    print(hex(id(nums)))
    nums[:] = nums[l-k:] + nums[:l-k]
    print(hex(id(nums)))
    return nums
print(rotate([1,2,3,4,5,6], 3))
