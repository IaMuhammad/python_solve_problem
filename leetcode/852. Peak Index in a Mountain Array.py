def peakIndexInMountainArray(arr):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        print(m, f'arr[m-1] {arr[m-1]} arr[m] {arr[m]}  arr[m+1] {arr[m+1]}', arr[m-1] < arr[m] and arr[m] < arr[m+1])

        if m == 0:
            if arr[m] > arr[m+1]:
                return m
            else:
                l = m+1

        elif arr[m-1] < arr[m] and arr[m] > arr[m+1]:
            return m
        
        elif arr[m-1] < arr[m]:
            l = m + 1
        else:
            r = m - 1

print(peakIndexInMountainArray([3,9,8,6,4]))