def countKDifference(nums, k):
    in1 = 1
    l = len(nums)
    c = 0
    for i in nums:
        for j in range(in1,l):
            print(f'i, j = {i} {nums[j]} k = {k} modul {abs(i - nums[j])} shart = {abs(i - nums[j]) == k}')
            if abs(i - nums[j]) == k:
                c += 1
        in1+=1
    return c

print(countKDifference([3,2,1,5,4], 2))
