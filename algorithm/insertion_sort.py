def sortArray(nums):
    for i in range(1, len(nums)):
        for j in range(i, -1, -1):
            if  j and nums[j] < nums[j-1]:
                x = nums.pop(j)
                nums.insert(j-1, x)
            else:
                break
    return nums

def insertion_sort_we(arr):
    i, l = 1, len(arr)
    while i < l:
        j = i-1
        while j > -1:
            if arr[i] >= arr[j]:
                x = arr.pop(i)
                arr.insert(j+1,x)
                break
            j -= 1
        i += 1

    return arr

print(insertion_sort_we([2, 43, 4, 65, 6, 78, 5, 45, 66, 8]))
