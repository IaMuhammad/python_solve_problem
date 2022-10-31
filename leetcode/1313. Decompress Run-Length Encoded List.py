def decompressRLElist(nums):
    length = len(nums)
    newList = []
    i = 0
    print(length / 2)

    while i < length:
        for j in range(0, nums[i]):
            newList.append(nums[i + 1])
        
        i += 2
    
    return newList

print(decompressRLElist([1,2,3,4,5,6]))