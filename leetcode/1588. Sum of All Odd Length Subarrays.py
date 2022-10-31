def sumOddLengthSubarrays(arr):
    i = 1
    c = 0
    ans = 0
    while i <= len(arr):
        ans += sum(arr[c:c+i:])
        c+=1
        if c + i > len(arr):
            i += 2
            c = 0
    
    return ans
        

l = [1,4,2,5,3]
print(sumOddLengthSubarrays(l))