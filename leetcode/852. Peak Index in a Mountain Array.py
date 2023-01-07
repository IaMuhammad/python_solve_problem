def peak_index_in_mountain_array_binary_search(arr: list[int]):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        print(m, f'arr[m-1] {arr[m - 1]} arr[m] {arr[m]}  arr[m+1] {arr[m + 1]}',
              arr[m - 1] < arr[m] and arr[m] < arr[m + 1])

        if m == 0:
            if arr[m] > arr[m + 1]:
                return m
            else:
                l = m + 1

        elif arr[m - 1] < arr[m] and arr[m] > arr[m + 1]:
            return m

        elif arr[m - 1] < arr[m]:
            l = m + 1
        else:
            r = m - 1


def peak_index_in_mountain_array_array(arr: list[int]):
    return arr.index(max(arr))


