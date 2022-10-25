input()
arr = list(map(int, input().split()))
c = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] ^ arr[j] == 0:
            c += 1

print(c)