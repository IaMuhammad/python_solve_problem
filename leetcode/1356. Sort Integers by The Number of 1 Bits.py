def sortByBits(arr):
    def takeSecond(elem):
        return elem[1]
    
    ans = []
    arr.sort()
    i = 0
    for el in arr:
        s = str(bin(el))[2:]
        print(el, s, s.count('1'))
        arr[i] = [el, s.count('1')]
        i+=1
    arr.sort(key=takeSecond)
    for i in arr:
        ans.append(i[0])
    return ans

arr = [1024,512,256,128,64,32,16,8,4,2,1]
print(sortByBits(arr))