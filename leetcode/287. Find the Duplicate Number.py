def findDuplicate(nums):
    nums = sorted(nums)

    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i+1]:
            answer = nums[i]
    
    return answer

num = [1,3,4,2,2]

print(findDuplicate(num))