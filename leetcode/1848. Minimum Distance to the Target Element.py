def getMinDistance(nums, target, start):
    i = 0
    ans = []
    for num in nums:
        if num == target:
            ans.append(abs(i - start))
        i += 1
    
    return min(ans)

n = [1,1,1,1,1,1,1,1,1,1]
t = 1
s = 9
print(getMinDistance(n, t, s))