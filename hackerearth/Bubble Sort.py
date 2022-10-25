def bubble_sort(arr):
    c, n = 0, len(arr)
    swapped = True
    while swapped:
        swapped = False
        c += 1
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return c
input()
print(bubble_sort(list(map(int, input().split()))))