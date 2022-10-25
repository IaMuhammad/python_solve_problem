def selection_sort_fe(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

def selection_sort_we(arr):
    i, l = 0, len(arr)
    while i < l:
        j = i+1
        minimum = i
        while j < l:
            if arr[minimum] > arr[j]:
                minimum = j
            j += 1
        arr[i], arr[minimum] = arr[minimum], arr[i]
        i += 1

    return arr

print(selection_sort_we([1,4,1,6,2,8]))