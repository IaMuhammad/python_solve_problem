def firstUniqChar(s):
    n = int()
    ind = 0
    for i in s:
        if s.count(i) == 1:
            return ind
        ind+=1
    return -1

print(firstUniqChar('leetcode'))