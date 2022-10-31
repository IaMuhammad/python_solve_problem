def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m =  l + (r - l)// 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    
    return l

print(searchInsert([1,3,5,6], 4))