def insertion_sort_fe(arr):
    l = len(arr)
    for i in range(1,l):
        for j in range(i-1,-1,-1):
            if arr[i] >= arr[j]:
                x = arr.pop(i)
                arr.insert(j+1, x)
                break

    return arr

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